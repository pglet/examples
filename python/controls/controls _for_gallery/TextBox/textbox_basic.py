import pglet
from pglet import Stack, Text, Textbox

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Basic textboxes", size="xLarge"),
    Stack(gap=25, horizontal=True, controls=[
      Textbox(label='Standard'),
      Textbox(label='Disabled', disabled=True)
    ]),
    Stack(gap=25, horizontal=True, controls=[
      Textbox(label='Read-only', read_only=True),  
      Textbox(label="With placeholder", placeholder='Please enter text here')
    ])
])

page.add(stack)