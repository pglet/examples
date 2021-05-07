import pglet
from pglet import Stack, Text, Checkbox

page = pglet.page()

def checkbox_with_on_change():

  def checkbox_changed(e):
    t.value = f"Checkbox value changed to {c.value}" 
    stack.update()

  c = Checkbox('Checkbox with on_change event', on_change=checkbox_changed)
  t = Text()
  stack = Stack(controls=[c, t])
  return stack


stack = Stack(gap=20, controls=[
    Text("Checkboxes", size="xLarge"),
    checkbox_with_on_change()
  ])

page.add(stack)

input("Press Enter to exit...")