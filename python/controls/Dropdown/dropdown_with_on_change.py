import pglet
from pglet import Dropdown
from pglet import dropdown
with pglet.page("myapp") as page:
  page.clean()
  from pglet import Text

  def dropdown_changed(e):
        t.value = f"Dropdown changed to {d.value}" 
        page.update()

  d = Dropdown(width=100, on_change=dropdown_changed, options=[
    dropdown.Option('Red'),
    dropdown.Option('Green'),
    dropdown.Option('Blue')
  ])

  t = Text()

  page.add(d, t)

  input()

