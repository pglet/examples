Import-Module pglet

Connect-PgletApp -Name "pglet-textbox" -ScriptBlock {

    $controls = @(
      TextBox -Multiline -AutoAdjustHeight -Label "Multiline textbox with auto-adjust height"
      TextBox -Underlined -Label "Underlined textbox:"
      TextBox -Borderless -Label "Borderless textbox"
      TextBox -Prefix 'https://' -Label "Textbox with prefix"
      TextBox -Suffix 'px' -Label "Textbox with sufix"
      TextBox -Prefix 'https://' -Suffix '.com' -Label "Textbox with prefix and suffix"
    )
  
    $pglet_page.add($controls)
  }