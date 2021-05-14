import pglet
from pglet import Stack, Text, Tabs, Tab, Textbox, Button

page = pglet.page()
#page.horizontal_align = 'stretch'

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

stack = Stack(controls=[  
    Text("Solid tabs", size="xLarge"),
    solid_tabs 
])
    
page.add(stack)