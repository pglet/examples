import pglet
from pglet import Checkbox, Text

with pglet.page("checkbox-with-change-event") as page:
  def checkbox_changed(e):
    t.value = f"Checkbox value changed to {c.value}" 
    t.update()

  c = Checkbox("Checkbox with 'change' event", on_change=checkbox_changed)
  t = Text()

  page.add(c, t)
  input()