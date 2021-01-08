Import-Module pglet

Connect-PgletApp -Name 'hello-app' -ScriptBlock {
    Invoke-Pglet "add text value='Hello to connection $PGLET_CONNECTION_ID!'"
}