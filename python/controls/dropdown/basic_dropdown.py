import pglet
from pglet import Dropdown, dropdown, Button, Text
with pglet.page("basic-dropdown") as page:
  
  def button_clicked(e):
    t.value = f"Dropdown value is:  {dd.value}"
    page.update()
  
  t = Text()
  b = Button(text='Submit', on_click=button_clicked)
  dd = Dropdown(width=100, options=[
    dropdown.Option('Red'),
    dropdown.Option('Green'),
    dropdown.Option('Blue')
  ])
  page.add(dd, b, t)

  input()

