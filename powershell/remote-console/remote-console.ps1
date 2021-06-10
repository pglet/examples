Import-Module pglet

$ErrorActionPreference = "stop"

$pageName = "ps-shell-$(hostname)"
if ($env:PGLET_PAGE) {
    $pageName = $env:PGLET_PAGE
}

if (-not $env:PGLET_PERMISSIONS) {
    throw "'PGLET_PERMISSIONS' environment variable is not set. Specify the list of GitHub usernames, teams or email addresses being able to access this app, for example PGLET_PERMISSIONS=`"User1, user2@somemail.com`"."
}

Connect-PgletApp -Name $pageName -Permissions $env:PGLET_PERMISSIONS -ScriptBlock {
    $ErrorActionPreference = 'stop'

    $page = $PGLET_PAGE
    $page.Title = "PowerShell Remote Console"
    $page.HorizontalAlign = 'stretch'

    # Textbox with a command entered
    $cmd = TextBox -Placeholder "Type PowerShell command and click Run or press ENTER..." -Width '100%'

    # Event handler to call when "Run" button is clicked or Enter pressed
    $run_on_click = {
        $cmd_text = $cmd.value
        if ([string]::IsNullOrWhitespace($cmd_text)) {
            return
        }

        # disable textbox and Run button, add spinner while the command is evaluating
        $cmd.value = ''
        $command_panel.disabled = $true
        $results.controls.insert(0, (Text $cmd_text -BgColor 'neutralLight' -Padding 10))
        $results.controls.insert(1, (Spinner))
        $page.update()

        try {

            # run the command
            $result = Invoke-Expression $cmd_text

            # if result is Array present it as Grid; otherwise Text
            if ($result -is [System.Array]) {
                $result_control = Grid -Compact -Items $result
            } else {
                $result_control = Text -Value ($result | Out-String) -Pre -Padding 10
            }
        } catch {
            $result_control = Text -Value "$_" -Pre -Padding 10 -Color 'red'
        }

        # re-enable controls and replace spinner with the results
        $command_panel.disabled = $false
        $results.controls.removeAt(1)
        $results.controls.insert(1, $result_control)
        $page.update()
    }
    
    # container for command textbox and Run button
    $command_panel = Stack -Horizontal -OnSubmit $run_on_click -Controls @(
        $cmd
        Button -Text "Run" -Primary -Icon 'Play' -OnClick $run_on_click
    )

    # results container
    $results = Stack

    # "main" view combining all controls together
    $view = @(
        $command_panel
        Stack -Controls @(
            Stack -Horizontal -VerticalAlign Center -Controls @(
                Text 'Results' -Size large
                Button -Icon 'Clear' -Title 'Clear results' -OnClick {
                    $results.controls.clear()
                    $results.update()
                }
            )
            $results
        )
    )

    # display the "main" view onto the page
    $page.add($view)
}