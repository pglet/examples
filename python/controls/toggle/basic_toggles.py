import pglet
from pglet import Toggle, Button, Text
with pglet.page("basic-toggles") as page:
  def button_clicked(e):
        t.value = f"Toggles values are:  {t1.value}, {t2.value}, {t3.value}, {t4.value}."
        page.update()

  t = Text()
  t1 = Toggle(label='Enabled and checked', value=True)
  t2 = Toggle(label='Enabled and unchecked')
  t3 = Toggle(disabled=True, label='Disabled and checked', value=True)
  t4 = Toggle(disabled=True, label='Disabled and unchecked')
  b = Button(text='Submit', on_click=button_clicked)
  page.add(t1, t2, t3, t4, b, t)

  input()