from re import T
import pglet
from pglet import Stack, Text, Textbox

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("TextBox with icon", size="xLarge"),
    Textbox(label='With an icon', icon='Emoji2'),
    Textbox(label='With custom icon', icon='mail', icon_color='red')
])

page.add(stack)