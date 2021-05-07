import pglet
from pglet import Stack, Text, ChoiceGroup, Button, Textbox
from pglet import choicegroup

page = pglet.page()

def change_items_in_choicegroup():

  def add_clicked(e):
    cg.options.append(choicegroup.Option(option_name.value))
    option_name.value = ''
    option_name.error_message = ''
    stack.update()

  def delete_clicked(e):
    option_found = False
    for option in cg.options:
        if option.key == option_name.value:
          cg.options.remove(option)
          option_found = True
          option_name.error_message = ''
    if option_found == False:
        option_name.error_message = 'Option not found'
    option_name.value = ''
    stack.update() 

  cg = ChoiceGroup()
  option_name = Textbox(placeholder='Enter option name')
  add = Button("Add", on_click=add_clicked)
  delete = Button("Delete", on_click=delete_clicked)
  stack = Stack(controls = [cg, Stack(horizontal=True, controls=[option_name, add, delete])])
  return stack
 
stack = Stack(gap=20, controls=[
    Text("Change items in choicegroup options", size="xLarge"),
    change_items_in_choicegroup()
  ])

page.add(stack)

input("Press Enter to exit...")