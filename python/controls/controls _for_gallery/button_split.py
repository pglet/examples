import pglet
from pglet import Stack, Text, Button
from pglet import button

page = pglet.page()

stack = Stack(controls=[
    Text("Split buttons", size="xLarge"),
    Stack(horizontal=True, controls=[
      Button(split=True, text='Standard', menu_items=[
        button.MenuItem('Email message', icon='Mail'),
        button.MenuItem('Calendar event', icon='Calendar')
      ]),
      Button(split=True, primary=True, text='Primary', menu_items=[
        button.MenuItem('Email message', icon='Mail'),
        button.MenuItem('Calendar event', icon='Calendar')
      ])
    ])
])

page.add(stack)