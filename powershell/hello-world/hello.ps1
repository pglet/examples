Import-Module pglet

$p = Connect-PgletPage "hello"
$p.clean($true)
$p.add((Text -Value 'Hello, world!'))