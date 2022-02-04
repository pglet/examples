import pglet
from pglet import SpinButton, Button, Text
with pglet.page("basic-spinbutton") as page:
  def button_clicked(e):
        t.value = f"Spinbutton value is:  {sb.value}."
        page.update()

  t = Text()
  sb = SpinButton(width='50%', label='Default SpinButton')
  b = Button(text='Submit', on_click=button_clicked)
  page.add(sb, b, t)

  input()
  
