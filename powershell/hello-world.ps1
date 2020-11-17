import-module pglet

connect-pgletpage

invoke-pglet "add text value='Hello, world!'"
invoke-pglet "add button id=ok text=OK"

while($true) {
  $e = Wait-PgletEvent
  if ($e.Target -eq 'ok' -and $e.Name -eq 'click') {

    invoke-pglet "clean page"
    invoke-pglet "add text value=`"That's all, folks!`""
    return
  }
}

disconnect-pglet