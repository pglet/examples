# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function buttons() {
  pglet_send "
add
stack gap=30

  stack
    text value='Regular buttons' size=large
    stack horizontal
      button text='Standard'
      button disabled text='Standard disabled'
    stack horizontal
      button primary text='Primary'
      button primary disabled text='Primary disabled'

  stack
    text value='Compound buttons' size=large
    stack horizontal
      button compound text='Compound' secondaryText='This is a secondary text'
      button primary compound text='Primary compound' secondaryText='This is a secondary text'
  
  stack
    text value='Buttons with icon' size=large
    stack horizontal
      button primary icon='AddFriend' text='Create account'
      button icon='Add' text='New item'    
      button icon='Delete' text='Delete'
  
  stack
    text value='Toolbar buttons' size=large
    stack horizontal
      button toolbar icon='Add' text='New item'
      button toolbar icon='Mail' text='Send'
      button toolbar icon='ChevronDown' text='Show example'
      button toolbar icon='Delete' iconColor=red text='Delete'

  stack
    text value='Icon only buttons' size=large
    stack horizontal
      button icon='Emoji2' title=Emoji!
      button icon='Calendar' title=Calendar!

  stack
    text value='Link buttons' size=large
    stack horizontal
      button action icon='Globe' text='Pglet website' url='https://pglet.io' newWindow
      button icon='MyMoviesTV' text='Go to Disney' url='https://disney.com' newWindow

  stack
    text value='Context menu buttons' size=large
    stack horizontal
      button icon='Add' text='New item'
        item text='Email message' icon='Mail'
        item text='Calendar event' icon='Calendar'
      button text='Button with sub-menus'
        item text='New' icon='Add'
          item text='Email message' icon='Mail'
          item text='Calendar event' icon='Calendar'
        item text='Share' icon='Share' split
          item text='Share to Twitter' key='sharetotwitter'
          item text='Share to Facebook' key='sharetofacebook'
          item text='Share to Somewhere' disabled
          item text='Share to Email' key='sharetoemail'
            item text='Share to Outlook'
            item text='Share to Gmail'
        item divider
        item text='To to Pglet' icon='Globe' iconColor=green url='https://pglet.io' newWindow secondaryText='New window'

  stack
    text value='Split buttons' size=large
    stack horizontal
      button split text='Standard'
        item text='Email message' icon='Mail'
        item text='Calendar event' icon='Calendar'
      button split primary text='Primary'
        item text='Email message' icon='Mail'
        item text='Calendar event' icon='Calendar'
  "
}

pglet_app "index" "buttons"