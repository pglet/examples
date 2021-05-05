# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page horizontalAlign='stretch'"
  pglet_send "add
toolbar
  item text='New' icon='Add'
    item text='Email message' icon='Mail'
    item text='Calendar event' icon='Calendar'
  item id=share text='Share' icon='Share' split
    item text='Share to Twitter' data='sharetotwitter'
    item text='Share to Facebook' data='sharetofacebook'
    item text='Share to Somewhere' disabled
    item text='Share to Email' data='sharetoemail'
      item text='Share to Outlook'
      item text='Share to Gmail'
  item text='To to Google' icon='Globe' url='https://google.com' newWindow secondaryText='New window'
  overflow
    item text='Item 1' icon=Shop
    item text='Item 2' icon=Airplane
  far
    item text='Grid view' icon=Tiles iconOnly
    item text=Info icon=Info iconColor=green iconOnly
  "
}

pglet_app "index" "main"