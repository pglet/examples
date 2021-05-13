import pglet
from pglet import Stack, Text, Toggle

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Toggles with inline label", size="xLarge"),
    Stack(gap=25, horizontal=True, controls=[
        Toggle(inline=True, label='With inline label', on_text='On', off_text='Off'),
        Toggle(disabled=True, inline=True, label='Disabled with inline label', on_text='On', off_text='Off')
    ]),
    Stack(gap=25, controls=[
        Toggle(inline=True, label='With inline label and without onText and offText'),
        Toggle(disabled=True, inline=True, label='Disabled with inline label and without onText and offText')
    ])
])

page.add(stack)