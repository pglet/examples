#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
set -e

# include Pglet library
. $DIR/../pglet.sh

PGLET_PUBLIC=false pglet_page

#echo "$PGLET_CONNECTION_ID"

function hello() {
    echo "Hello!"
}

pglet_send "add text value='Hello, world!'"
pglet_send "add button id=ok text=OK"

#events=("ok click hello")
#pglet_dispatch_events "${events[@]}"

pglet_dispatch_events "ok click hello"

# while true
# do
#     pglet_wait_event
#     if [[ "$PGLET_EVENT_TARGET" == "ok" && "$PGLET_EVENT_NAME" == "click" ]]; then
#         pglet_send "clean page"
#         pglet_send "add text value=\"That's all, folks!\""
#         exit 0
#     fi
# done