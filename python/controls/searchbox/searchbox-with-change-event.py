import pglet
from pglet import SearchBox, Text

with pglet.page("searchbox-with-change-event") as page:
   
  def searchbox_changed(e):
    t.value = f'You have searched for {sb.value}.'
    page.update()

  sb = SearchBox(placeholder='Search something...', on_change=searchbox_changed)
  t = Text()

  page.add(sb, t)

  input()