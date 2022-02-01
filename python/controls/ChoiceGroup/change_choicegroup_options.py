import pglet
from pglet import ChoiceGroup
from pglet import choicegroup
with pglet.page("myapp") as page:
  page.clean()
  from pglet import Textbox, Button, Stack
  def add_clicked(e):
    cg.options.append(choicegroup.Option(new_option.value))
    new_option.value = ''
    stack.update()

  cg = ChoiceGroup()
  new_option = Textbox(placeholder='Enter new item name')
  add = Button("Add", on_click=add_clicked)
  stack = Stack(controls = [cg, Stack(horizontal=True, controls=[new_option, add])])

  page.add(stack)

  input()