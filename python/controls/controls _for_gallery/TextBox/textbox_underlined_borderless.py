import pglet
from pglet import Stack, Text, Textbox

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Underlined and borderless Textboxes", size="xLarge"),
    Stack(gap=25, controls=[
      Textbox(label='Underlined', underlined=True, placeholder='Enter text here'),
      Textbox(label='Borderless', borderless=True, placeholder='Enter text here')
    ])
])

page.add(stack)