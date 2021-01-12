# Constants
PGLET_VER="0.1.12"        # Pglet version required by this script

# Default session variables:
PGLET_EXE=""             # full path to Pglet executable
PGLET_CONNECTION_ID=""   # the last page connection ID.
PGLET_PAGE_URL=""        # the last page URL.
PGLET_EVENT_TARGET=""    # the last received event target (control ID).
PGLET_EVENT_NAME=""      # the last received event name.
PGLET_EVENT_DATA=""      # the last received event data.

# Parameters:
#   $1 - page name
# Variables:
#   PGLET_WEB         - makes the page available as public at pglet.io service or a self-hosted Pglet server
#   PGLET_PRIVATE     - makes the page available as private at pglet.io service or a self-hosted Pglet server
#   PGLET_SERVER      - connects to the page on a self-hosted Pglet server
#   PGLET_TOKEN       - authentication token for pglet.io service or a self-hosted Pglet server

function pglet_page() {
    local pargs=(page)

    if [[ "$1" != "" ]]; then
        pargs+=($1)
    fi

    if [[ "$PGLET_WEB" == "true" ]]; then
        pargs+=(--web)
    fi

    if [[ "$PGLET_SERVER" != "" ]]; then
        pargs+=(--server $PGLET_SERVER)
    fi

    if [[ "$PGLET_TOKEN" != "" ]]; then
        pargs+=(--token $PGLET_TOKEN)
    fi

    if [[ "$PGLET_NO_WINDOW" != "" ]]; then
        pargs+=(--no-window)
    fi

    # execute pglet and get page connection ID
    local page_results=`$PGLET_EXE "${pargs[@]}"`
    IFS=' ' read -r PGLET_CONNECTION_ID PGLET_PAGE_URL <<< "$page_results"

    echo "Page URL: $PGLET_PAGE_URL"
}

function __pglet_start_session() {
    echo "Started session: $1"
    PGLET_CONNECTION_ID=$1
    local fn=$2

    eval "$fn"
}

function pglet_app() {
    local pargs=(app)

    if [[ $# -eq 1 ]]; then
        # only hander function specified
        local fn=$1
    elif [[ $# -eq 2 ]]; then
        # page name and hander function specified
        pargs+=($1)
        local fn=$2
    else
        echo "Error: wrong number of arguments"
        exit 1
    fi

    if [[ "$PGLET_WEB" == "true" ]]; then
        pargs+=(--web)
    fi

    if [[ "$PGLET_SERVER" != "" ]]; then
        pargs+=(--server $PGLET_SERVER)
    fi

    if [[ "$PGLET_TOKEN" != "" ]]; then
        pargs+=(--token $PGLET_TOKEN)
    fi

    if [[ "$PGLET_NO_WINDOW" != "" ]]; then
        pargs+=(--no-window)
    fi

    # reset vars
    PGLET_PAGE_URL=""

    # execute pglet
    $PGLET_EXE "${pargs[@]}" |
    {
        while read -r session_id
        do
            if [[ "$PGLET_PAGE_URL" == "" ]]; then
                PGLET_PAGE_URL="$session_id"
                echo "Page URL: $PGLET_PAGE_URL"
            else
                __pglet_start_session $session_id $fn &
            fi
        done
    }
}

function pglet_send() {
    if [[ $# -eq 1 ]]; then
        local conn_id=$PGLET_CONNECTION_ID
        local cmd=$1
    elif [[ $# -eq 2 ]]; then
        local conn_id=$1
        local cmd=$2
    else
        echo "Error: wrong number of arguments"
        exit 1
    fi

    # send command
    echo "$cmd" > "$conn_id"

    # take result if command doesn't end with "f" (fire-and-forget)
    if [[ "$cmd" =~ ^[[:space:]]*[A-Za-z]+f ]]; then
        return
    fi

    # read result
    local firstLine="true"
    local result_value=""
    IFS=''
    while read -r line; do
        if [[ $firstLine == "true" ]]; then
            IFS=' ' read -r result_status result_value <<< "$line"
            firstLine="false"
            if [[ "$result_status" == "error" ]]; then
                echo "Error: $result_value"
                exit 2
            fi
        else
            result_value="$line"
        fi
        echo "$result_value"
    done <"$conn_id"
}

function pglet_add() {
    pglet_send "add $1"
}

function pglet_addf() {
    pglet_send "addf $1"
}

function pglet_set() {
    pglet_send "set $1"
}

function pglet_setf() {
    pglet_send "setf $1"
}

function pglet_set_value() {
    pglet_send "set $1 value=\"${2//\"/\\\"}\""
}

function pglet_set_valuef() {
    pglet_send "setf $1 value=\"${2//\"/\\\"}\""
}

function pglet_get_value() {
    pglet_send "get $1 value"
}

function pglet_show() {
    pglet_send "set $1 visible=true"
}

function pglet_hide() {
    pglet_send "set $1 visible=false"
}

function pglet_enable() {
    pglet_send "set $1 enabled=true"
}

function pglet_disable() {
    pglet_send "set $1 enabled=false"
}

function pglet_clean() {
    pglet_send "clean $1"
}

function pglet_remove() {
    pglet_send "remove $1"
}

function pglet_wait_event() {
    if [[ "$1" != "" ]]; then
        local conn_id=$1
    else
        local conn_id=$PGLET_CONNECTION_ID
    fi

    IFS=' ' read PGLET_EVENT_TARGET PGLET_EVENT_NAME PGLET_EVENT_DATA < "$conn_id.events"
}

function pglet_dispatch_events() {
  # https://askubuntu.com/questions/992439/bash-pass-both-array-and-non-array-parameter-to-function

  #echo "count: $#"

  arr=("$@")
  IFS=' '
  while true
  do
    pglet_wait_event
    for evt in "${arr[@]}";
    do
      IFS=' ' read -r et en fn <<< "$evt"
      if [[ "$PGLET_EVENT_TARGET" == "$et" && "$PGLET_EVENT_NAME" == "$en" ]]; then
        eval "$fn"
        return
      fi      
      #echo "$et - $en - $fn"
    done
  done
}

function __pglet_install() {
    if [ "$(uname -m)" != "x86_64" ]; then
        echo "Error: Unsupported architecture $(uname -m). Only x64 binaries are available." 1>&2
        exit 1
    fi

    if [ "$OS" = "Windows_NT" ]; then
        echo "Error: Bash for Windows is not supported." 1>&2
        exit 1
    else
        case $(uname -s) in
        Darwin) target="darwin-amd64.tar.gz" ;;
        *) target="linux-amd64.tar.gz" ;;
        esac
    fi

    # check if pglet.exe is in PATH already (development mode)
    if command -v pglet &> /dev/null
    then
        PGLET_EXE=`which pglet`
        return
    fi

    # check if there is Pglet aready installed
    local pglet_dir="$HOME/.pglet"
    local pglet_bin="$pglet_dir/bin"
    PGLET_EXE="$pglet_bin/pglet"

    local ver="$PGLET_VER"
    local installed_ver=""

    if [ -f "$PGLET_EXE" ]; then
        installed_ver=$($PGLET_EXE --version)
    fi

    #echo "Installed version: $installed_ver"

    if [[ "$installed_ver" != "$ver" ]]; then
        printf "Installing Pglet v$ver..."

        if [ ! -d "$pglet_bin" ]; then
            mkdir -p "$pglet_bin"
        fi

        local pglet_url="https://github.com/pglet/pglet/releases/download/v${ver}/pglet-${target}"
        local tempTar="$HOME/.pglet/pglet.tar.gz"
        curl -fsSL $pglet_url -o $tempTar
        tar zxf $tempTar -C $pglet_bin
        rm $tempTar

        #echo "OK"
    fi
}

__pglet_install