# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function theme() {
  pglet_send "set page horizontalAlign='stretch'"
  pglet_send "
add
stack gap=30

  toggle id=theme label='Theme' inline offText=Light onText=Dark

  stack
    text value='Context menu buttons example' size=large
    stack horizontal
      button icon='Add' text='New item'
        item text='Email message' icon='Mail'
        item text='Calendar event' icon='Calendar'
      button split primary icon='Add' text='New item'
        item text='Email message' icon='Mail'
        item text='Calendar event' icon='Calendar'

  stack
    text value='Regular buttons example' size=large
    stack horizontal
      button text='Standard'
      button disabled text='Standard disabled'
    stack horizontal
      button primary text='Primary'
      button primary disabled text='Primary disabled'
  "

  while true
  do
      pglet_wait_event
      if [[ "$PGLET_EVENT_TARGET" == "theme" && "$PGLET_EVENT_DATA" == "true" ]]; then
        # Dark theme
        pglet_send "set page themePrimaryColor='#3ee66d' themeTextColor='#edd2b7' themeBackgroundColor='#262626'"
      elif [[ "$PGLET_EVENT_TARGET" == "theme" && "$PGLET_EVENT_DATA" == "false" ]]; then
        # Light theme
        pglet_send "set page themePrimaryColor='' themeTextColor='' themeBackgroundColor=''"        
      fi
  done
}

pglet_app "index" "theme"