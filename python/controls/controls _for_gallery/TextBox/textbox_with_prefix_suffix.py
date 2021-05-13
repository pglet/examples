import pglet
from pglet import Stack, Text, Textbox

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("TextBox with prefix and/or suffix", size="xLarge"),
    Stack(gap=25, horizontal=True, controls=[
      Textbox(label='With prefix', prefix='https://'),
      Textbox(label='With suffix', suffix='.com')
    ]),
    Stack(horizontal=True, controls=[
      Textbox(label='With prefix and suffix', prefix='https://', suffix='.com')
    ])
])

page.add(stack)