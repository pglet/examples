import pglet
from pglet import Callout, Button, Text, Stack, Toggle, Slider, Dropdown, dropdown
with pglet.page("callout-with-directional-hint") as page:
      
  def button_clicked(e):
        c.beak = beak.value
        c.gap = int(gap_space.value)
        c.beak_width = int(beak_width.value)
        c.position = position.value
        c.visible = True
        page.update()


  beak = Toggle(label='Show beak', value=True)
  gap_space = Slider(width='50%', label='Gap space', show_value=True, min=0, max=30, step=1, value=0)
  beak_width = Slider(width='50%', label='Beak width', show_value=True, min=10, max=50, step=1, value=16)
  show_callout = Button(text='Show callout', on_click=button_clicked)
  position = Dropdown(width=100, label='Position', value='bottomLeft', options=[
    dropdown.Option('topLeft'),
    dropdown.Option('topCenter'),
    dropdown.Option('topRight'),
    dropdown.Option('bottomLeft'),
    dropdown.Option('bottomCenter'),
    dropdown.Option('bottomRight')
  ])

  stack = Stack(horizontal_align='center', width='50%', controls=[show_callout])

  page.add(beak, gap_space, beak_width, position, stack)

  c = Callout(target=show_callout.uid, width=200, height=100, visible = False, controls=[
        Stack(controls=[
          Text(size='large', align='center', value='Callout title'),
          Text(size='small', align='center', value='This is a basic callout')
      ])
  ])
  
  page.add(c)

  input()
  
  
