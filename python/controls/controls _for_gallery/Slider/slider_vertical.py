import pglet
from pglet import Stack, Text, Slider

page = pglet.page()

stack = Stack(width='50%', controls=[
    Text("Vertical sliders", size='xLarge'),
    Stack(horizontal=True, height='200px', controls=[
        Slider(vertical=True, label='Default slider'),
        Slider(vertical=True, label='Default disabled slider', disabled=True),
        Slider(vertical=True, label='Slider with value', show_value=True, value=4),
        Slider(vertical=True, label='Slider with formatted value', show_value=True, min=0, max=100, value=40, value_format='{value}%'),
        Slider(vertical=True, show_value=True, label='Origin from zero', min=-5, max=15, step=1, value=-2)
    ])
])

page.add(stack)