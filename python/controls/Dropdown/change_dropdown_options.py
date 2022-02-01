import pglet
from pglet import Dropdown
from pglet import dropdown
with pglet.page("myapp") as page:
  page.clean()
  from pglet import Textbox, Button, Stack

  def add_clicked(e):
    d.options.append(dropdown.Option(new_option.value))
    d.value = new_option.value
    new_option.value = ''
    page.update()



  d = Dropdown()
  new_option = Textbox(placeholder='Enter new item name')
  add = Button("Add", on_click=add_clicked)
  stack = Stack(controls = [d, Stack(horizontal=True, controls=[new_option, add])])

  page.add(stack)

  input()

