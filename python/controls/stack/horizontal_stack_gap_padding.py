import pglet
from pglet import Stack, Slider, Text
with pglet.page("horizontal-stack-gap-padding") as page:

  bg_color = '#ddddee'
  page.horizontal_align = 'stretch'

  def items(count):
    items = []
    for i in range(1, count + 1):
      items.append(Text(value=i, align='center', vertical_align='center', width=30, height=30, bgcolor='BlueMagenta10', color='white', padding=5))
    return items

  def gap_slider_change(e):
    spacing_stack.gap = int(e.control.value)
    spacing_stack.update()

  def padding_slider_change(e):
    spacing_stack.padding = e.control.value
    spacing_stack.update()

  gap_slider = Slider("Gap between items", min=0, max=50, step=1, value=0, show_value=True, on_change=gap_slider_change)
  padding_slider = Slider("Stack padding", min=0, max=50, step=1, value=0, show_value=True, on_change=padding_slider_change)
  spacing_stack = Stack(horizontal=True, bgcolor=bg_color, gap=0, controls=items(5))
  
  page.add(gap_slider, padding_slider, spacing_stack)

  input()
  
  
