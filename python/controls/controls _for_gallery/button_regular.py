import pglet
from pglet import Stack, Text, Button

page = pglet.page()

stack = Stack(controls=[
    Text('Regular buttons', size='xLarge'),
    Stack(horizontal=True, controls=[
      Button("Standard"),
      Button("Standard disabled", disabled=True)
    ]),
    Stack(horizontal=True, controls=[
      Button("Primary", primary=True),
      Button("Primary disabled", primary=True, disabled=True)
    ])
])

page.add(stack)