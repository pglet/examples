from datetime import datetime
import pglet
from pglet import Stack, Text, DatePicker, Button

page = pglet.page()

picker = DatePicker(label="Pick or enter a date: ", allow_text_input=True)

def on_click(e):
        print(e.control.value)

stack = Stack(controls=[
        Text('DatePicker that allows text input', size='xLarge'),
        Stack(controls=[
            DatePicker(label="Pick or enter a date: ", allow_text_input=True),
            DatePicker(label="Allow text input with placeholder", placeholder='Select date...', allow_text_input=True)
        ]),
    ])

page.add(stack)