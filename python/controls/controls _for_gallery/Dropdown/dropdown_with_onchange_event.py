import pglet
from pglet import Stack, Text, Dropdown
from pglet import dropdown

page = pglet.page()

def dropdown_with_on_change():

  def dropdown_changed(e):
    t.value = f"Dropdown value changed to {dd.value}" 
    stack.update()
  
  dd = Dropdown(on_change=dropdown_changed, options=[
    dropdown.Option('Red'),
    dropdown.Option('Green'),
    dropdown.Option('Blue')
  ])

  t = Text()
  stack = Stack(controls=[dd, t])
  return stack

stack = Stack(gap=20, controls=[
    Text("Dropdown with on_change event", size="xLarge"),
    dropdown_with_on_change()
  ])

page.add(stack)

input("Press Enter to exit...")