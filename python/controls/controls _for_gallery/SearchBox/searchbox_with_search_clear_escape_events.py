import pglet
from pglet import Stack, Text, SearchBox

page = pglet.page()

def searchbox_with_search_clear_escape():

  def enter_clicked(e):
    messages.controls.append(Text(f'You have searched for {sb.value}.'))
    sb.value = ''
    stack.update()
  
  def clear_or_esc_clicked(e):
    messages.controls.append(Text('You have cleared the box.'))
    stack.update()

  sb = SearchBox(placeholder='Search something and click Enter, X or Esc', 
    on_search=enter_clicked, on_clear=clear_or_esc_clicked)
    
  messages = Stack()
  stack = Stack(controls=[sb, messages])
  return stack

stack = Stack(gap=20, controls=[
        Text("SearchBox with Search, Clear and Escape events", size="xLarge"),
        searchbox_with_search_clear_escape()
    ])



page.add(stack)

input("Press Enter to exit...")