import pglet
from pglet import Stack, Text, ChoiceGroup
from pglet import choicegroup

page = pglet.page()

def choicegroup_with_on_change():

  def choicegroup_changed(e):
    t.value = f"ChoiceGroup value changed to {cg.value}" 
    stack.update()
  
  cg = ChoiceGroup(label='Select color', on_change=choicegroup_changed, options=[
    choicegroup.Option('Red'),
    choicegroup.Option('Green'),
    choicegroup.Option('Blue')
  ])

  t = Text()
  stack = Stack(controls=[cg, t])
  return stack

stack = Stack(gap=20, controls=[
    Text("ChoiceGroup with on_change event", size="xLarge"),
    choicegroup_with_on_change()
  ])

page.add(stack)

input("Press Enter to exit...")