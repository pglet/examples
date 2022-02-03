import pglet
from pglet import Button
with pglet.page("icon-only-buttons") as page:
  page.add(
    Button(icon='Emoji2', title='Emoji!'),
    Button(icon='Calendar', title='Calendar!'))