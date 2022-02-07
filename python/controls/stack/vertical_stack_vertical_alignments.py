import pglet
from pglet import Stack, Text
with pglet.page("vertical-stack-vertical-alignments") as page:

  bg_color = '#ddddee'
  page.horizontal_align = 'stretch'

  def items(count):
    items = []
    for i in range(1, count + 1):
      items.append(Text(value=i, align='center', vertical_align='center', width=30, height=30, bgcolor='BlueMagenta10', color='white', padding=5))
    return items

  def vertical_stack(vert_align):
        return Stack(width='20%', controls=[
            Text(value=vert_align),
            Stack(vertical_align=vert_align, horizontal_align='center', height=300, gap=20, bgcolor=bg_color, controls=items(3))
        ])

  page.add(Stack(horizontal=True, horizontal_align='space-between', width='100%', controls=[
            vertical_stack('start'),
            vertical_stack('center'),
            vertical_stack('end'),
            vertical_stack('space-between'),
            vertical_stack('space-around'),
            vertical_stack('space-evenly')
        ]))

  input()
  
  
