import pglet
from pglet import Stack, Text, Dropdown, Button, Textbox
from pglet import dropdown

page = pglet.page()

def change_items_in_dropdown():

  def add_clicked(e):
    dd.options.append(dropdown.Option(option_name.value))
    dd.value = option_name.value
    option_name.value = ''
    stack.update()

  def delete_clicked(e):
    for option in dd.options:
        if option.key == dd.value:
            dd.options.remove(option) 
    stack.update() 

  dd = Dropdown(width=100)
  option_name = Textbox(placeholder='Enter option name')
  add = Button("Add", on_click=add_clicked)
  delete = Button("Delete selected", on_click=delete_clicked)
  stack = Stack(horizontal_align='start', controls = [
      Stack(horizontal=True, controls=[option_name, add]),
      dd,
      delete])
  return stack
 
stack = Stack(gap=20, controls=[
    Text("Change items in dropdown options", size="xLarge"),
    change_items_in_dropdown()
  ])

page.add(stack)

input("Press Enter to exit...")