import pglet
from pglet import Stack, Text, Button

page = pglet.page()

stack = Stack(controls=[
    Text("Toolbar buttons", size="xLarge"),
    Stack(horizontal=True, controls=[
      Button(text="New item", toolbar=True, icon='Add'),
      Button(text="Send", toolbar=True, icon='Mail'),
      Button(text="Show example", toolbar=True, icon='ChevronDown'),
      Button(text="Delete", toolbar=True, icon_color='red', icon='Delete')
    ])
])

page.add(stack)