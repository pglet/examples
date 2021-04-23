# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "
add
stack gap=30

  stack
    text value='Nav with groups' size=large
    nav
      item text='Actions'
        item expanded text='New'
          item key='email' text='Email message' icon='Mail'
          item key='calendar' text='Calendar event' icon='Calendar' iconColor=salmon
      item text='Share' collapsed
        item disabled key=share text='Share to Facebook' icon='Share'
        item key=twitter text='Share to Twitter'
      item text='Links' collapsed
        item text='Pglet website' icon='NavigateExternalInline' url='https://pglet.io' newWindow
        item text='Google website' icon='NavigateExternalInline' url='https://google.com' newWindow

  stack
    text value='Nav without groups' size=large
    nav
      item
        item expanded text='New'
          item key='email' text='Email message' icon='Mail'
          item key='calendar' text='Calendar event' icon='Calendar'
          item text='More options'
            item key='option' text='Web component' icon='WebComponents'
        item expanded text=Share
          item key=facebook text='Share on Facebook' icon='Share'
          item key=twitter text='Share to Twitter' icon='Share'
  "
}

pglet_app "index" "main"