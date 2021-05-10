import pglet
from pglet import Stack, Text, Link

page = pglet.page()

def link_with_on_click():
    
  def link_clicked(e):
    l.data += 1
    t.value = f"Link clicked {l.data} time(s)"
    stack.update()

  l = Link(value='Click on the link', on_click=link_clicked, title='Click me!', data=0)
  t = Text()
  stack = Stack(controls=[l, t])
  return stack

stack = Stack(controls=[
    Text('Link with on_click event', size='xLarge'),
    link_with_on_click()
])

page.add(stack)

input("Press Enter to exit...")