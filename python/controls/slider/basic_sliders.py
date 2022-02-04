import pglet
from pglet import Slider
with pglet.page("basic-sliders") as page:
  page.add(
    Slider(width='50%', label='Default slider'),
    Slider(width='50%', label='Default disabled slider', disabled=True))