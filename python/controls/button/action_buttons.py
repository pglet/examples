import pglet
from pglet import Button, Stack
with pglet.page("action-buttons") as page:
  page.add(Stack(horizontal=True, controls=[
    Button(action=True, icon='ChevronLeftEnd6'),
    Button(action=True, icon='ChevronLeftSmall'),
    Button(action=True, icon='ChevronRightSmall'),
    Button(action=True, icon='ChevronRightEnd6')
  ]))