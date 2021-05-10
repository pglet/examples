import pglet
from pglet import Stack, Text, Dropdown
from pglet import dropdown

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Basic Dropdown", size="xLarge"),
    Dropdown(options=[
        dropdown.Option('Red'),
        dropdown.Option('Green'),
        dropdown.Option('Blue')
    ])
  ])

page.add(stack)