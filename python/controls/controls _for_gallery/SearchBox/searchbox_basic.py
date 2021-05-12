import pglet
from pglet import Stack, Text, SearchBox

page = pglet.page()

stack = Stack(gap=20, controls=[
    Stack(horizontal=True, gap=25, controls=[
        Stack(controls=[
            Text("Default searchbox", size="xLarge"),
            SearchBox(),
        ]),
        Stack(controls=[
            Text("Underlined SearchBox", size="xLarge"),
            SearchBox(underlined=True, placeholder='Search files and folders'),
        ])
    ])
    ])

page.add(stack)