import pglet
from pglet import Stack, Text, SearchBox

page = pglet.page()

def searchbox_with_change():

  def searchbox_changed(e):
    t.value = f'You have searched for {sb.value}.'
    stack.update()

  sb = SearchBox(placeholder='Search something...', on_change=searchbox_changed)
  t = Text()
  stack = Stack(controls=[sb, t])
  return stack

stack = Stack(gap=20, controls=[
        Text("SearchBox with Change event", size="xLarge"),
        searchbox_with_change()
    ])

page.add(stack)

input("Press Enter to exit...")