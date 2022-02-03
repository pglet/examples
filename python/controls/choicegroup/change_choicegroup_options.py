import pglet
from pglet import ChoiceGroup
from pglet import choicegroup
with pglet.page("myapp") as page:
  page.clean()
  from pglet import Textbox, Button, Stack

  def find_option(option_name):
    for option in cg.options:
        if option_name == option.key:
          return option          
    return None

  def add_clicked(e):
    cg.options.append(choicegroup.Option(option_textbox.value))
    option_textbox.value = ''
    page.update()

  def delete_clicked(e):
    option = find_option(cg.value)
    if option !=None:
      cg.options.remove(option)   
      page.update()

  cg = ChoiceGroup()
  option_textbox = Textbox(placeholder='Enter new item name')
  
  add = Button("Add", on_click=add_clicked)
  delete = Button("Delete selected", on_click=delete_clicked)
  stack = Stack(controls = [cg, Stack(horizontal=True, controls=[option_textbox, add, delete])])

  page.add(stack)

  input()