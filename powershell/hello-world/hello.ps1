Import-Module pglet
Connect-PgletPage "hello"
Invoke-Pglet "clean page"
Invoke-Pglet "add text value='Hello, world!'"