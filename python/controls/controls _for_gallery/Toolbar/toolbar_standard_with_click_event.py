import pglet
from pglet import Stack, Text, Toolbar, Message
from pglet import toolbar

page = pglet.page()
page.horizontal_align = 'stretch'

message = Message(visible=False, dismiss=True)

def item_clicked(e):
    #page.controls.insert(0, Message(value=f'Menu item "{e.control.text}" was clicked', dismiss=True))
    message.value = f'Menu item "{e.control.text}" was clicked'
    message.visible = True
    page.update()

standard_toolbar = Toolbar(items=[
        toolbar.Item(text='New', icon='Add', items=[
            toolbar.Item(text='Email message', icon='Mail', on_click=item_clicked),
            toolbar.Item(text='Calendar event', icon='Calendar', on_click=item_clicked)
            ]),  
        toolbar.Item(text='Share', icon='Share', split=True, items=[
            toolbar.Item(text='Share to Twitter', on_click=item_clicked),
            toolbar.Item(text='Share to Facebook', on_click=item_clicked),
            toolbar.Item(text='Share to Somewhere', disabled=True, on_click=item_clicked),
            toolbar.Item(text='Share to Email', data='sharetoemail', items=[
                toolbar.Item(text='Share to Outlook', on_click=item_clicked),
                toolbar.Item(text='Share to Gmail', on_click=item_clicked)
            ])
        ]),
        toolbar.Item(text='To to Google', icon='Globe', url='https://google.com', new_window=True, secondary_text='New window')
        ], 
        overflow=[
            toolbar.Item(text='Item 1', icon='Shop', on_click=item_clicked),
            toolbar.Item(text='Item 2', icon='Airplane', on_click=item_clicked)
        ], 
        far=[
            toolbar.Item(text='Grid view', icon='Tiles', icon_only=True, on_click=item_clicked),
            toolbar.Item(text='Info', icon='Info', icon_color='green', icon_only=True, on_click=item_clicked)
    ])

stack = Stack(gap=30, controls=[
      Stack(controls=[
          message,
          Text("Standard toolbar with Click event", size="xLarge"),
          standard_toolbar
      ])
  ])

page.add(stack)

input("Press Enter to exit...")