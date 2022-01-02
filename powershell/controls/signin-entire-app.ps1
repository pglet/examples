Import-Module pglet

Connect-PgletApp -Permissions "*" -ScriptBlock {
    $page = $PGLET_PAGE
    $page.theme = 'dark'

    $loggedUser = Text "Welcome, $($page.userLogin)"

    $page.onSignin = {
        Write-Trace "Sign in event"
        $loggedUser.value = $page.userLogin
        $page.update()
    }

    $page.onSignout = {
        Write-Trace "Sign out event"
        $loggedUser.value = "Not signed in"
        $page.update()
    }

    $signoutButton = Button -Primary -Text "Sign out" -OnClick {
        $page.signout()
    }
    
    $page.add($loggedUser, $signoutButton)
}