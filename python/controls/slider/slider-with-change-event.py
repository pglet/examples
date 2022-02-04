import pglet
from pglet import Slider, Text
with pglet.page("slider-with-change-event") as page:

  def slider_changed(e):
    t.value = f"Slider changed to {int(s.value)}"
    page.update()

  t = Text()
  s = Slider(width='50%', label="Slider with 'change' event", on_change=slider_changed, data=0)
  
  page.add(s, t)

  input()