import pglet
from pglet import Stack, Text, Button

page = pglet.page()

stack = Stack(controls=[
    Text("Link buttons", size="xLarge"),
    Stack(horizontal=True, controls=[
      Button(action=True, icon='Globe', text='Pglet website',url='https://pglet.io', new_window=True),
      Button(icon='MyMoviesTV', text='Go to Disney',        url='https://disney.com', new_window=True)
    ])
])

page.add(stack)