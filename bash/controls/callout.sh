# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page padding=0"
  pglet_send "add
stack horizontal
  button id=showCallout text='Show bottom callout'
  button id=showCallout2 text='Show right callout'
callout id=callout1 target='showCallout' focus=true visible=false
  stack padding=20 width=300
    text value='Choose your style' size=xlarge
    choicegroup
      option key=red
      option key=green
      option key=blue
    stack horizontal
      button id=yes primary text=Yes
      button id=no text=No
callout id=callout2 target='showCallout2' beak=true cover=false position=rightTop pagePadding=0 visible=false
  stack padding=20 width=300 height=100
    text value='That\'s a button callout!' size=xlarge"

  while true
  do
      pglet_wait_event
      if [[ "$PGLET_EVENT_TARGET" == "showCallout" ]]; then
        pglet_send "set callout1 visible=true"
      elif [[ "$PGLET_EVENT_TARGET" == "showCallout2" ]]; then
        pglet_send "set callout2 visible=true"
      fi
  done
}

pglet_app "index" "main"