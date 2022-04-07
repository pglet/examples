import pglet
from pglet import ChoiceGroup, choicegroup, Textbox, Button, Stack
with pglet.page("change-choicegroup-options") as page:

  def find_option(option_name):
    for option in cg.options:
        if option.key == option_name:
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