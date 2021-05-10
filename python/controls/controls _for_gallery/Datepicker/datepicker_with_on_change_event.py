from datetime import datetime
import pglet
from pglet import Stack, Text, DatePicker

page = pglet.page()

now = datetime.now()

def datepicker_changed(e):
        t.value = f"DatePicker value changed to {e.control.value}"
        stack.update()

t = Text()

stack = Stack(controls=[
        Text('Basic DatePicker controls', size='xLarge'),
        Stack(controls=[
            DatePicker("Select a date:", value=now, on_change=datepicker_changed),
            t
        ]),
    ])

page.add(stack)

input("Press Enter to exit...")