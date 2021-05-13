from re import T
import pglet
from pglet import Stack, Text, Textbox

page = pglet.page()

def on_change(e):
    if e.control.value == '':
        e.control.error_message = 'Please enter value'
    else:
        e.control.error_message = ''
    stack.update()

stack = Stack(gap=20, controls=[
    Text("Required textboxes with Change event and error message", size="xLarge"),
    Textbox(width='50%', label='Required:', required=True, on_change=on_change, error_message='Please enter value'),
    Textbox(width='50%', required=True, on_change=on_change, error_message='Please enter value')
])

page.add(stack)

input("Press Enter to exit...")