import pglet
from pglet import Stack, Text, Slider

page = pglet.page()

stack = Stack(width='50%', controls=[
    Text("Horizontal sliders", size="xLarge"),
    Slider(label='Default slider'),
    Slider(label='Default disabled slider', disabled=True),
    Slider(label='Slider with value', show_value=True, value=4),
    Slider(label='Slider with formatted value', show_value=True, min=0, max=100, value=40, value_format='{value}%'),
    Slider(show_value=True, label='Origin from zero', min=-5, max=15, step=1, value=-2)
])

page.add(stack)