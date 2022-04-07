import pglet
from pglet import Button, Stack
with pglet.page("action-button") as page:
  page.add(Stack(horizontal=True, controls=[
    Button(action=True, icon='AddFriend', text='Create account')
  ]))