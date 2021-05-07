import pglet
from pglet import Stack, Text, Checkbox

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Checkboxes", size="xLarge"),
    Checkbox(label='Unchecked checkbox', value=False),
    Checkbox(label='Checked checkbox', value=True),
    Checkbox(label='Disabled checkbox', disabled=True),
    Checkbox(label="Checkbox with rendered box_side='End'", box_side='End')
  ])

page.add(stack)