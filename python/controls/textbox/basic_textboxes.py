import pglet
from pglet import Textbox, Button, Text
with pglet.page("basic-textboxes") as page:
  def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()

  t = Text()
  tb1 = Textbox(label='Standard')
  tb2 = Textbox(label='Disabled', disabled=True, value='First name')
  tb3 = Textbox(label='Read-only', read_only=True, value='Last name')  
  tb4 = Textbox(label="With placeholder", placeholder='Please enter text here')
  tb5 = Textbox(label='With an icon', icon='Emoji2')
  b = Button(text='Submit', on_click=button_clicked)
  page.add(tb1, tb2, tb3, tb4, tb5, b, t)

  input()
  
  
