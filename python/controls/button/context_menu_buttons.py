import pglet
from pglet import Button, Stack, button
with pglet.page("context-menu-buttons") as page:
  page.add(Stack(horizontal=True, controls=[
    Button(icon='Add', text='New item', menu_items=[
      button.MenuItem(text='Email message', icon='Mail'),
      button.MenuItem(text='Calendar event', icon='Calendar')
    ]),
    Button(text='Button with sub-menus', menu_items=[
      button.MenuItem(text='New', icon='Add', sub_menu_items=[
      button.MenuItem(text='Email message', icon='Mail'),
      button.MenuItem(text='Calendar event', icon='Calendar')
    ]),
      button.MenuItem(text='Share', icon='Share', split=True, sub_menu_items=[
        button.MenuItem(text='Share to Twitter'),
        button.MenuItem(text='Share to Facebook'),
        button.MenuItem('Share to Somewhere'),
        button.MenuItem('Share to email', sub_menu_items=[
          button.MenuItem('Share to Outlook'),
          button.MenuItem('Share to Gmail')
        ])
      ]),
      button.MenuItem(divider=True),
      button.MenuItem(text='To Pglet', icon='Globe', icon_color='green', url='https://pglet.io', new_window=True, secondary_text='New Window')
    ]),
  ]))