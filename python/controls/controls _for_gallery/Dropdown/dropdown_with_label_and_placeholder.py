import pglet
from pglet import Stack, Text, Dropdown
from pglet import dropdown

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Dropdown with label and placeholder", size="xLarge"),
    Dropdown(label='Color', placeholder='What\'s your favourite color?', options=[
        dropdown.Option('Red'),
        dropdown.Option('Green'),
        dropdown.Option('Blue')
    ])
  ])

page.add(stack)