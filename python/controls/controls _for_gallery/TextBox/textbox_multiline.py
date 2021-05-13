import pglet
from pglet import Stack, Text, Textbox

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Multiline textboxes", size="xLarge"),
    Stack(controls=[
        Stack(gap=25, horizontal=True, controls=[
            Textbox(label='standard', multiline=True),
            Textbox(label='disabled', multiline=True, disabled=True)
        ]),
        Stack(gap=25, horizontal=True, controls=[
            Textbox(label='With auto adjusted height', multiline=True, auto_adjust_height=True) #need auto-adjusted height property
        ])
    ])
])

page.add(stack)