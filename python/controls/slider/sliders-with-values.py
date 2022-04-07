import pglet
from pglet import Slider, Button, Text
with pglet.page("sliders-with-values") as page:

  def button_clicked(e):
        t.value = f"Sliders values are:  {s1.value}, {s2.value}, {s3.value}."
        page.update()

  t = Text()
  s1 = Slider(width='50%', label='Slider with value', show_value=True, value=4)
  s2 = Slider(width='50%', label='Slider with formatted value', show_value=True, min=0, max=100, value=40, value_format='{value}%')
  s3 = Slider(width='50%', show_value=True, label='Origin from zero', min=-5, max=15, step=1, value=-2)
  
  b = Button(text='Submit', on_click=button_clicked)
  page.add(s1, s2, s3, b, t)

  input()