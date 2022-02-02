import pglet
from pglet import Dropdown
from pglet import dropdown
with pglet.page("myapp") as page:
  page.clean()
  from pglet import Textbox, Button, Stack

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
    option = find_option(option_textbox.value)
    if option !=None:
      d.options.remove(option)    
    else:
      option_textbox.error_message = 'Option not found.'
    
    option_textbox.value = ''
    page.update()

  d = Dropdown()
  option_textbox = Textbox(placeholder='Enter item name')
  add = Button("Add", on_click=add_clicked)
  delete = Button("Delete", on_click=delete_clicked)
  stack = Stack(controls = [d, Stack(horizontal=True, controls=[option_textbox, add, delete])])

  page.add(stack)

  input()

