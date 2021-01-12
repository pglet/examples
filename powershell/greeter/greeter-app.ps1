Import-Module pglet

Connect-PgletApp -Name 'greeter-app' -ScriptBlock {
  $txt_name = Invoke-Pglet "add textbox label='Your name' description='Please provide your full name'"
  $btn_hello = Invoke-Pglet "add button primary text='Say hello'"
  
  while($true) {
    $e = Wait-PgletEvent
    if ($e.Target -eq $btn_hello -and $e.Name -eq 'click') {
      $name = Invoke-Pglet "get $txt_name value"
      Invoke-Pglet "clean page"
      Invoke-Pglet "add text value='Hello, $name!'"
      return
    }
  }
}