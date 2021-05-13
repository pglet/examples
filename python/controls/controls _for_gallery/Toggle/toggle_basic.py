import pglet
from pglet import Stack, Text, Toggle

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Basic toggles", size="xLarge"),
    Stack(gap=25, horizontal=True, controls=[
        Toggle(label='Enabled and checked', value=True),
        Toggle(label='Enabled and unchecked')
    ]),
    Stack(gap=25, horizontal=True, controls=[
        Toggle(disabled=True, label='Disabled and checked', value=True),
        Toggle(disabled=True, label='Disabled and unchecked')
    ])
])

page.add(stack)