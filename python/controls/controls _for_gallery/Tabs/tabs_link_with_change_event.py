import pglet
from pglet import Stack, Text, Tabs, Tab, Message

page = pglet.page()
#page.horizontal_align = 'stretch'

message = Message(visible=False, dismiss=True)

def tabs_changed(e):
    message.visible = True
    message.value = f'Tabs changed to "{e.control.value}", count increased'
    e.control.tabs[2].count +=1
    page.update()

link_tabs = Tabs(margin=10, on_change=tabs_changed, tabs=[
    Tab(text='Regular tab', controls=[
        Stack(horizontal=True, controls=[
            Text('This is tab1'),
            Text('This is tab1 - line2')
          ])
      ]),
    Tab(icon='Globe', text='Tab with icon', controls=[
        Stack(gap=10, controls=[
            Text(value='This is tab2'),
            Text(value='This is tab2 - line2')
        ])
      ]),
    Tab(text='Tab with icon and count', icon='Ringer', count=0, controls=[
        Stack(gap=10, controls=[
            Text('This is tab3'),
            Text('This is tab3 - line2')
          ])
      ])      
    ])

stack = Stack(controls=[  
    message,
    Text("Link tabs with Change event", size="xLarge"),
    link_tabs
])
    
page.add(stack)

input("Press Enter to exit...")