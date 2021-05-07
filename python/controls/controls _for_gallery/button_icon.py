import pglet
from pglet import Stack, Text, Button

page = pglet.page()

stack = Stack(controls=[
    Text("Icon buttons", size="xLarge"),
    Stack(horizontal=True, controls=[
      Button("Create account", icon='AddFriend', primary=True),
      Button("New item", icon='Add'),
      Button("Delete", icon='Delete')
    ])
])

page.add(stack)