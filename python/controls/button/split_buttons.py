import pglet
from pglet import Button, Stack
with pglet.page("myapp") as page:
    page.clean()
    from pglet import button
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