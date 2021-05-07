import pglet
from pglet import Stack, Text, Button

page = pglet.page()

stack = Stack(controls=[
    Text("Icon only buttons", size="xLarge"),
    Stack(horizontal=True, controls=[
      Button(icon='Emoji2', title='Emoji!'),
      Button(icon='Calendar', title='Calendar!')
    ])
])

page.add(stack)