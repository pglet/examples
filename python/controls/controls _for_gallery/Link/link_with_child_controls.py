import pglet
from pglet import Stack, Text, Link, Icon

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Link with child controls", size="xLarge"),
    Link(url='http://google.com', controls=[
        Icon('Globe'),
        Text(' Text control in a link')
    ]),
  ])

page.add(stack)