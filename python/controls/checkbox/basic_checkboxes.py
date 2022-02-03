import pglet
from pglet import Checkbox, Button, Text
with pglet.page("basic-checkboxes") as page:
  def button_clicked(e):
        t.value = f"Checkboxes values are:  {c1.value}, {c2.value}, {c3.value}, {c4.value}."
        page.update()

  t = Text()
  c1 = Checkbox(label='Unchecked by default checkbox', value=False)
  c2 = Checkbox(label='Checked by default checkbox', value=True)
  c3 = Checkbox(label='Disabled checkbox', disabled=True)
  c4 = Checkbox(label="Checkbox with rendered box_side='end'", box_side='end')
  b = Button(text='Submit', on_click=button_clicked)
  page.add(c1, c2, c3, c4, b, t)

  input()
  
  
