import pglet
from pglet import Stack, Text, SearchBox

page = pglet.page()

stack = Stack(gap=20, controls=[
        Text("SearchBox with custom icon", size="xLarge"),
        SearchBox(placeholder='Filter something by', icon='Filter', icon_color='red')
    ])

page.add(stack)