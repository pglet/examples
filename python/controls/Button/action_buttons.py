import pglet
from pglet import Button, Stack
with pglet.page("myapp") as page:
    page.clean()
    page.add(Stack(horizontal=True, controls=[
      Button(action=True, text='<'),
      Button(action=True, text='<<'),
      Button(action=True, text='>'),
      Button(action=True, text='>>'),
    ]))