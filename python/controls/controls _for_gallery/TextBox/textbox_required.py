from re import T
import pglet
from pglet import Stack, Text, Textbox, Button

page = pglet.page()


def on_change(e):
    if e.control.value == '':
        e.control.error_message = 'Please enter value'
    else:
        e.control.error_message = ''
    stack.update()



stack = Stack(gap=20, controls=[
    Text("Required textboxes", size="xLarge"),
    Textbox(label='Required:', required=True, on_change=on_change, error_message='Please enter value'),
    Textbox(required=True, on_change=on_change, error_message='Please enter value')
])

page.add(stack)

input("Press Enter to exit...")