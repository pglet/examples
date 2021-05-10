from datetime import datetime
import pglet
from pglet import Stack, Text, DatePicker

page = pglet.page()

now = datetime.now()

stack = Stack(controls=[
        Text('Basic DatePicker controls', size='xLarge'),
        Stack(controls=[
            DatePicker("DatePicker with label"),
            DatePicker("DatePicker with label and value", value=now),
            DatePicker("Required DatePicker", required=True)
        ]),
    ])

page.add(stack)