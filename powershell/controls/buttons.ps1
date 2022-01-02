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

        # context menu buttons
        Button -Icon "Add" -Text "New item" -MenuItems @(
            MenuItem -Text "Email message" -Icon "Mail"
            MenuItem -Text "Calendar event" -Icon "Calendar"
        )

        $dialog
    )

    $page.add($view)
}