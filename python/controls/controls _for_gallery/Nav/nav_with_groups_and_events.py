import pglet
from pglet import Stack, Text, Nav, Message
from pglet import nav

page = pglet.page()

message = Message(visible=False, dismiss=True)

def menu_item_expanded(e):
    message.value = f'Menu item "{e.data}" was expanded'
    message.visible = True
    page.update()

def menu_item_collapsed(e):
    message.value = f'Menu item "{e.data}" was collapsed'
    message.visible = True
    page.update()

def menu_item_changed(e):
    message.value = f'Menu item was changed to "{nav.value}"'
    message.visible = True
    page.update()

nav = Nav(on_collapse=menu_item_collapsed, on_expand=menu_item_expanded, on_change=menu_item_changed, items=[
        nav.Item(text='Actions', items=[
            nav.Item(expanded=True, text='New', items=[
                nav.Item(key='email', text='Email message', icon='Mail'),
                nav.Item(key='calendar', text='Calendar event', icon='Calendar', icon_color='salmon')
            ]),
            nav.Item(text='Share', items=[
                nav.Item(disabled=True, key='share', text='Share to Facebook', icon='Share'),
                nav.Item(key='twitter', text='Share to Twitter')
            ]),
            nav.Item(text='Links', items=[   
                nav.Item(text='Pglet website', icon='NavigateExternalInline', url='https://pglet.io', new_window=True),
                nav.Item(text='Google website', icon='NavigateExternalInline', url='https://google.com', new_window=True) 
            ])
        ])
    ])

stack = Stack(gap=30, controls=[
      Stack(controls=[
          Text("Nav with groups and Expand, Collapse and Change events", size="xLarge"),
          message,
          nav
      ])
  ])

page.add(stack)

input("Press Enter to exit...")