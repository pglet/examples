Import-Module pglet

Connect-PgletApp -Name "pglet-buttons" -ScriptBlock {
    $page = $PGLET_PAGE

    $dialog = Dialog -Title "Hello" -SubText "Button clicked!"

    $view = @(
        Text -Value "Standard button" -Size Large
        Stack -Horizontal -Controls @(
            Button -Text "Standard" -OnClick {
                $dialog.Open = $true
                $page.update()
            }
            Button -Disabled -Text "Standard disabled"
        )

        Text -Value "Primary button" -Size Large
        Stack -Horizontal -Controls @(
            Button -Primary -Text "Primary"
            Button -Primary -Disabled -Text "Primary disabled"
        )

        Text -Value "Compound button" -Size Large
        Stack -Horizontal -Controls @(
            Button -Compound -Text "Compound" -SecondaryText "This is a secondary text"
            Button -Compound -Primary -Text "Primary compound" -SecondaryText "This is a secondary text"
        )

        $dialog
    )

    $page.add($view)
}

"add
  stack horizontal
    button text='Standard'
    button disabled text='Standard disabled'
  stack horizontal
    button primary text='Primary'
    button primary disabled text='Primary disabled'
  stack horizontal
    button compound text='Compound' secondaryText='This is a secondary text'
    button primary compound text='Primary compound' secondaryText='This is a secondary text'
  stack horizontal
    button icon='Add' text='Button with icon'
    button primary icon='Delete' text='Delete'
  stack horizontal
    button toolbar icon='Add' text='New item'
    button toolbar icon='Mail' text='Send'
    button toolbar icon='ChevronDown' text='Show example'
    button toolbar icon='Delete' iconColor=red text='Delete'
  stack horizontal
    button icon='Emoji2' title=Emoji!
    button icon='Calendar' title=Calendar!
  stack horizontal
    button ghost icon='AddFriend' text='Create account'
    button ghost icon='Add' text='New item'
  stack horizontal
    button action icon='Globe' text='Pglet website' url='https://pglet.io' newWindow
    button icon='MyMoviesTV' text='Go to Disney' url='https://disney.com' newWindow
  stack horizontal
    button text='Button with menu'
      item id=new text='New' icon='Add'
        item text='Email message' icon='Mail'
        item text='Calendar event' icon='Calendar'
      item id=share text='Share' icon='Share'
        item id=twitter text='Share to Twitter' data='sharetotwitter'
        item id=facebook text='Share to Facebook' data='sharetofacebook'
      item
        item data='key1'
    button primary split text='Primary with split'
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
      item text='To to Google' icon='Globe' iconColor=green url='https://google.com' newWindow secondaryText='New window'
"