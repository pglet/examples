import pglet
from pglet import SearchBox, Stack, Text

with pglet.page("searchbox-with-search-clear-and-escape-events") as page:
   
  def enter_clicked(e):
    messages.controls.append(Text(f'You have searched for {sb.value}.'))
    sb.value = ''
    page.update()

  def clear_or_esc_clicked(e):
    sb.value = ''
    messages.controls.append(Text('You have cleared the box.'))
    page.update()

  sb = SearchBox(width=300, placeholder='Search something and click Enter, X or Esc', on_search=enter_clicked, on_clear=clear_or_esc_clicked)
  messages = Stack()

  page.add(sb, messages)

  input()