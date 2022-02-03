import pglet
from pglet import Link
with pglet.page("myapp") as page:
  page.clean()
  from pglet import Text
  def link_clicked(e):
    l.data += 1
    t.value = f"Link clicked {l.data} time(s)"
    page.update()

  l = Link(value='Link with on_click event', on_click=link_clicked, title='Click me!', data=0)
  t = Text()
  
  page.add(l, t)
  input()