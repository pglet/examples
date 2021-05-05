Import-Module pglet

$page = Connect-PgletPage "greeter"
$page.clean()

$txt_name = TextBox -Label 'Your name' -Description 'Please provide your full name'
$btn_hello = Button -Primary -Text 'Say hello' -OnClick {
  $page.controls.clear()
  $page.controls.add(((Text -Value "Hello, $($txt_name.value)!")))
  $page.update()
}

$page.add($txt_name, $btn_hello)

Switch-PgletEvents