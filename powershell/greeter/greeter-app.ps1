Import-Module pglet

$main = {

  $page = $PGLET_PAGE

  $txt_name = TextBox -Label 'Your name' -Description 'Please provide your full name'
  $btn_hello = Button -Primary -Text 'Say hello' -OnClick {
    $page.controls.clear()
    $page.controls.add(((Text -Value "Hello, $($txt_name.value)!")))
    $page.update()
  }

  $page.add($txt_name, $btn_hello)
}

Connect-PgletApp -Name 'greeter-app' -ScriptBlock $main