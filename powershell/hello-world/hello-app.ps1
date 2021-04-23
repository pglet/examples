Import-Module pglet

$main = {
    $PGLET_PAGE.add((Text -Value "Hello to connection $($PGLET_PAGE.connection.pipeID)!"))
}

Connect-PgletApp -Name 'hello-app' -ScriptBlock $main