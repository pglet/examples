# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page gap=20"
  pglet_send "add
button id=open text='Open panel'
panel blocking lightDismiss autodismiss=false id=panel title='Missing Subject' type=small 
  choicegroup
    option key=Red
    option key=Green
    option key=Blue
  footer
    stack horizontal
      button id=yes primary text=Yes
      button id=no text=No
"

  while true
  do
    pglet_wait_event
    echo "Event: $PGLET_EVENT_TARGET $PGLET_EVENT_NAME $PGLET_EVENT_DATA"

    if [[ "$PGLET_EVENT_TARGET" == "open" ]]; then
      pglet_send "set panel open=true"
    elif [[ "$PGLET_EVENT_TARGET" == "panel" && "$PGLET_EVENT_NAME" == "dismiss" ]] ; then
      pglet_send "set panel open=false"
    elif [[ "$PGLET_EVENT_TARGET" == "panel:yes" ]] || [[ "$PGLET_EVENT_TARGET" == "panel:no" ]]; then
      pglet_send "set panel open=false"
    fi
  done
}

pglet_app "index" "main"