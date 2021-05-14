import pglet
from pglet import Stack, Text, Toolbar
from pglet import toolbar

page = pglet.page()
page.horizontal_align = 'stretch'


inverted_toolbar = Toolbar(inverted=True, items=[
        toolbar.Item(text='New', icon='Add', items=[
            toolbar.Item(text='Email message', icon='Mail'),
            toolbar.Item(text='Calendar event', icon='Calendar')
            ]),  
        toolbar.Item(text='Share', icon='Share', split=True, items=[
            toolbar.Item(text='Share to Twitter'),
            toolbar.Item(text='Share to Facebook'),
            toolbar.Item(text='Share to Somewhere', disabled=True),
            toolbar.Item(text='Share to Email', data='sharetoemail', items=[
                toolbar.Item(text='Share to Outlook'),
                toolbar.Item(text='Share to Gmail')
            ])
        ]),
        toolbar.Item(text='To to Google', icon='Globe', url='https://google.com', new_window=True, secondary_text='New window')
        ], 
        overflow=[
            toolbar.Item(text='Item 1', icon='Shop'),
            toolbar.Item(text='Item 2', icon='Airplane')
        ], 
        far=[
            toolbar.Item(text='Grid view', icon='Tiles', icon_only=True),
            toolbar.Item(text='Info', icon='Info', icon_color='green', icon_only=True)
    ])

stack = Stack(gap=30, controls=[
      Stack(controls=[
          Text("Inverted toolbar for top menu", size="xLarge"),
          Stack(bgcolor='magentaLight', controls=[
            inverted_toolbar
          ])
      ])
  ])

page.add(stack)