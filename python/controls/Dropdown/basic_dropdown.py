import pglet
from pglet import Dropdown
from pglet import dropdown
with pglet.page("myapp") as page:
  page.clean()
  from pglet import Button, Text
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

