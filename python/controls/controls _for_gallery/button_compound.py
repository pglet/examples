import pglet
from pglet import Stack, Text, Button

page = pglet.page()

stack = Stack(controls=[
    Text("Compound buttons", size="xLarge"),
    Stack(horizontal=True, controls=[
      Button("Compound", secondary_text='This is a secondary text', compound=True),
      Button("Primary compound", secondary_text='This is a secondary text', compound=True, primary=True)
    ])
])

page.add(stack)