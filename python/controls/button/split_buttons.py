import pglet
from pglet import Button, Stack, button
with pglet.page("split-buttons") as page:
  page.add(Stack(horizontal=True, controls=[
    Button(split=True, text='Standard', menu_items=[
      button.MenuItem('Email message', icon='Mail'),
      button.MenuItem('Calendar event', icon='Calendar')
    ]),
    Button(split=True, primary=True, text='Primary', menu_items=[
      button.MenuItem('Email message', icon='Mail'),
      button.MenuItem('Calendar event', icon='Calendar')
    ])
  ]))