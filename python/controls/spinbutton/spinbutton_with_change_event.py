import pglet
from pglet import SpinButton, Text
with pglet.page("spinbutton-with-change-event") as page:
  def spinbutton_changed(e):
    t.value = f"SpinButton value changed to {sb.value}" 
    page.update()

  t = Text()
  sb = SpinButton(width='50%', label='Default SpinButton', on_change=spinbutton_changed)
  page.add(sb, t)

  input()
  
