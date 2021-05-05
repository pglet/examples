# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page horizontalAlign='stretch'"
  pglet_send "add
stack gap=30

  stack
    text value='Link tabs' size=large
    tabs id=t1 margin=10
      tab key=10 text='Regular tab'
        stack horizontal
          text value='This is tab1'
          text value='This is tab1 - line2'
      tab id=tab2 key=20 icon=Globe text='Tab with icon'
        stack gap=10
          text value='This is tab2'
          text value='This is tab2 - line2'
      tab key=30 text='Tab with icon and count' icon=Ringer count=30
        stack gap=10
          text value='This is tab3'
          text value='This is tab3 - line2'

  stack
    text value='Solid tabs' size=large
    tabs solid margin=10px
      tab text=JavaScript icon=Code count=10
        textbox label='Some textbox'
      tab text='C#' count=30
        button text='Hello button!'
      tab text=Python count=0
        text value='Just text...'
  "
}

pglet_app "index" "main"