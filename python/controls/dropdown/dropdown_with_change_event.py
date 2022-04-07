import pglet
from pglet import Dropdown, dropdown, Text
with pglet.page("dropdown-with-change-event") as page:

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

