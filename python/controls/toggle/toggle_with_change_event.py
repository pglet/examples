import pglet
from pglet import Toggle
with pglet.page("toggle-with-change-event") as page:
  def toggle_changed(e):
    if t.value:
      page.theme = 'dark'
    else:
      page.theme = 'light'
    page.update()

  t = Toggle(label="With 'change' event", on_text="Dark theme", off_text="Light theme", value=False, on_change=toggle_changed)

  page.theme = 'light'
  page.add(t)

  input()