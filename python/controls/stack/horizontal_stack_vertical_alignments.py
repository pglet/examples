import pglet
from pglet import Stack, Text
with pglet.page("horizontal-stack-vertical-alignments") as page:

  bg_color = '#ddddee'
  page.horizontal_align = 'stretch'

  def items(count):
    items = []
    for i in range(1, count + 1):
      items.append(Text(value=i, align='center', vertical_align='center', width=30, height=30, bgcolor='BlueMagenta10', color='white', padding=5))
    return items

  page.add(
        Text('start'),
        Stack(horizontal=True, vertical_align='start', height=100, bgcolor=bg_color, gap=20, controls=items(3)),
        Text('center'),
        Stack(horizontal=True, vertical_align='center', height=100, bgcolor=bg_color, gap=20, controls=items(3)),
        Text('end'),
        Stack(horizontal=True, vertical_align='end', height=100, bgcolor=bg_color, gap=20, controls=items(3)))

  input()
  
  
