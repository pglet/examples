import pglet
from pglet import Stack, Text, Link

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Links", size="xLarge"),
    Link(url='http://google.com', value='Visit Google', new_window=True),
    Link(value='Link without URL', size='large'),
    Link(url='http://google.com', value='Disabled link', disabled=True),
  ])

page.add(stack)