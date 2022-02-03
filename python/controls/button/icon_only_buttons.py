import pglet
from pglet import Button
with pglet.page("myapp") as page:
    page.clean()
    page.add(
      Button(icon='Emoji2', title='Emoji!'),
      Button(icon='Calendar', title='Calendar!'))