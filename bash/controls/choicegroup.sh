# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "add
stack gap=30

  stack
    text value='Basic ChoiceGroup' size=large  
    choicegroup label='Select color' value='green'
      option key=red
      option key=green
      option key=blue
  
  stack
    text value='ChoiceGroup with icons' size=large  
    choicegroup label='Pick one icon'
      option key=day text=Day icon=CalendarDay
      option key=week text=Week icon=CalendarWeek
      option key=month text=Month icon=Calendar
  "
}

pglet_app "index" "main"