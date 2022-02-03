import pglet
from pglet import Dropdown, dropdown, Textbox, Button, Stack
with pglet.page("change-dropdown-options") as page:

  def find_option(option_name):
    for option in d.options:
        if option_name == option.key:
          return option          
    return None

  def add_clicked(e):
    d.options.append(dropdown.Option(option_textbox.value))
    d.value = option_textbox.value
    option_textbox.value = ''
    page.update()

  def delete_clicked(e):
    option = find_option(d.value)
    if option !=None:
      d.options.remove(option)    
      page.update()

  d = Dropdown()
  option_textbox = Textbox(placeholder='Enter item name')
  add = Button("Add", on_click=add_clicked)
  delete = Button("Delete selected", on_click=delete_clicked)
  stack = Stack(controls = [d, Stack(horizontal=True, controls=[option_textbox, add, delete])])

  page.add(stack)

  input()

