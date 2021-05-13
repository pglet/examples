import pglet
from pglet import Stack, Text, Nav
from pglet import nav

page = pglet.page()

nav = Nav(items=[
              nav.Item(items=[
                nav.Item(expanded=True, text='New', items=[
                    nav.Item(key='email', text='Email message', icon='Mail'),
                    nav.Item(key='calendar', text='Calendar event', icon='Calendar'),
                    nav.Item(text='More options', items=[
                       nav.Item(key='option', text='Web component', icon='WebComponents')
                    ])
                ]),
                nav.Item(expanded=True, text='Share', items=[
                    nav.Item(key='facebook', text='Share on Facebook', icon='Share'),
                    nav.Item(key='twitter', text='Share to Twitter', icon='Share')
                ])
              ])
            ]) 

stack = Stack(gap=30, controls=[
      Stack(controls=[
          Text("Nav without groups", size="xLarge"),
          nav
      ])
  ])

page.add(stack)