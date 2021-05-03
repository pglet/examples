import pglet
from pglet import Stack, Text, Tabs, Tab, Message, Textbox, Button

def tabs(page):

  message = Message(dismiss=True, visible=False)

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

  solid_tabs = Tabs(solid=True, margin='10px', tabs=[
    Tab(text='JavaScript', icon='Code', count=10, controls=[
        Textbox(label='Some textbox')
        ]),
    Tab(text='C#', count=30, controls=[
        Button(text='Hello button!')
        ]),
    Tab(text='Python', count=0, controls=[
        Text(value='Just text...')
        ])        
    ])
       
  return Stack(gap=30, width='50%', controls=[
      message,
      Stack(controls=[
          Text("Link tabs with Change event", size="xLarge"),
          link_tabs
        ]),
      Stack(controls=[
          Text("Solid tabs", size="xLarge"),
          solid_tabs        
        ])
    ])

def main(page):
    
    page.title = "Tabs control samples"
    page.horizontal_align = 'stretch'
    page.update()
    page.add(tabs(page))

pglet.app("python-tabs", target=main)