from re import T
import pglet
from pglet import Stack, Text, Textbox

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Password with reveal button", size="xLarge"),
    Textbox(label='Password with reveal button', password=True)
])

page.add(stack)