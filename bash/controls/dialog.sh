# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page gap=20"
  pglet_send "add
button id=openMinimal text='Open minimal dialog'
dialog id=dialogMinimal title='Hello' close
  text value='Hi, are you OK?'
  footer
    button text=Yes
    button text=No

button id=openBasic text='Open basic dialog'
dialog id=dialogBasic blocking=false type=largeHeader title='Missing Subject' subText='Do you want to send this message without a subject?'
  footer
    button id=yes primary text=Yes
    button id=no text=No

button id=open text='Open dialog'
dialog id=dialog blocking=true type=close title='Missing Subject' subText='Do you want to send this message without a subject?' width=600
  choicegroup id=color
    option key=red
    option key=green
    option key=blue
  footer
    button id=yes primary text=Yes
    button id=no text=No
"

  while true
  do
    pglet_wait_event
    echo "Event: $PGLET_EVENT_TARGET $PGLET_EVENT_NAME $PGLET_EVENT_DATA"

    if [[ "$PGLET_EVENT_TARGET" == "openBasic" ]]; then
      pglet_send "set dialogBasic open=true"
    elif [[ "$PGLET_EVENT_TARGET" == "openMinimal" ]]; then
      pglet_send "set dialogMinimal open=true"
    elif [[ "$PGLET_EVENT_TARGET" == "open" ]]; then
      pglet_send "set dialog open=true"
    elif [[ "$PGLET_EVENT_TARGET" == "dialog:yes" ]] || [[ "$PGLET_EVENT_TARGET" == "dialog:no" ]]; then
      pglet_send "set dialog open=false"
    fi
  done
}

pglet_app "index" "main"