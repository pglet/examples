Import-Module pglet

Connect-PgletApp -Name "pglet-buttons" -ScriptBlock {
    $page = $PGLET_PAGE

    $dialog = Dialog -Title "Hello" -SubText "Button clicked!"

    $view = @(
        Text "Standard button" -Size Large
        Stack -Horizontal -Controls @(
            Button -Text "Standard - click me to see dialog" -OnClick {
                $dialog.Open = $true
                $page.update()
            }
            Button -Disabled -Text "Standard disabled"
        )

        Text "Primary button" -Size Large
        Stack -Horizontal -Controls @(
            Button -Primary -Text "Primary"
            Button -Primary -Disabled -Text "Primary disabled"
        )

        Text "Compound button" -Size Large
        Stack -Horizontal -Controls @(
            Button -Compound -Text "Compound" -SecondaryText "This is a secondary text"
            Button -Compound -Primary -Text "Primary compound" -SecondaryText "This is a secondary text"
        )

        Text "Buttons with icon" -Size Large
        Stack -Horizontal -Controls @(
            Button -Text "Create account" -Icon "AddFriend" -Primary
            Button -Text "New item" -Icon "Add"
            Button -Text "Delete" -Icon "Delete"
        )

        Text "Toolbar buttons" -Size Large
        Stack -Horizontal -Controls @(
            Button -Toolbar -Text "Send" -Icon "Mail"
            Button -Toolbar -Text "Show example" -Icon "ChevronDown"
            Button -Toolbar -Text "Delete" -Icon "Delete" -IconColor 'Red'
        )

        Text "Icon-only buttons" -Size Large
        Stack -Horizontal -Controls @(
            Button -Icon "Emoji2" -Title 'Emoji!'
            Button -Icon "Calendar" -Title 'Calendar!'
        )

        Text "Link buttons" -Size Large
        Stack -Horizontal -Controls @(
          Button -action -icon 'Globe' -text 'Pglet website' -url 'https://pglet.io' -newwindow
          Button -icon 'MyMoviesTV' -text 'Go to Disney' -url 'https://disney.com' -newwindow
        )            

        Text "Context menu buttons" -Size Large
        Button -Icon "Add" -Text "New item" -MenuItems @(
            MenuItem -Text "Email message" -Icon "Mail"
            MenuItem -Text "Calendar event" -Icon "Calendar"
        )

        Text "Button with sub-menus" -Size Large
        Button -Text 'Button with sub-menus' -MenuItems @(
          MenuItem -Icon "Add" -Text "New" -SubMenuItems @(
            MenuItem -Text "Email message" -Icon "Mail"
            MenuItem -Text "Calendar event" -Icon "Calendar"
          )
          MenuItem -Icon "Share" -Text "Share" -Split -SubMenuItems @(
            MenuItem -Text "Share to Twitter"
            MenuItem -Text "Share to Facebook"
            MenuItem "Share to Somewhere"
            MenuItem "Share to Email" -SubMenuItems @(
              MenuItem "Share to Outlook"
              MenuItem "Share to Gmail"
            )
            MenuItem -Divider
            MenuItem "To Pglet" -Icon "Globe" -IconColor "green" -Url "https://pglet.io" -NewWindow -SecondaryText "New Window"
          )          
        )

        Text "Split buttons" -Size Large
        Button -Split -Text "Standard" -MenuItems @(
          MenuItem -Text "Email message" -Icon "Mail" -OnClick { Write-Trace "Email message clicked!" }
          MenuItem -Text "Calendar event" -Icon "Calendar" -OnClick { Write-Trace "Calendar clicked!" }
        )
        Button -Split -Primary -Text "Primary" -MenuItems @(
          MenuItem -Text "Email message" -Icon "Mail"
          MenuItem -Text "Calendar event" -Icon "Calendar"
        )        

        $dialog
    )

    $page.add($view)
}