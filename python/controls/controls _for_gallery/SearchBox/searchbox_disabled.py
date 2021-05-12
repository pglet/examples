import pglet
from pglet import Stack, Text, SearchBox

page = pglet.page()

stack = Stack(gap=20, controls=[
        Text("Disabled SearchBox", size="xLarge"),
        SearchBox(disabled=True, placeholder='Search something...'),
        SearchBox(underlined=True, disabled=True, placeholder='Search something...')
    ])

page.add(stack)