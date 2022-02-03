from datetime import datetime
import pglet
from pglet import DatePicker
with pglet.page("myapp") as page:
  page.clean()
  from pglet import Button, Text
  def button_clicked(e):
    t.value = f"DatePickers values are:  {dp1.value}, {dp2.value}."
    page.update()

  now = datetime.now()
  t = Text()
  b = Button(text='Submit', on_click=button_clicked)
  dp1 = DatePicker(label="Start date", value=now, width=150)
  dp2 = DatePicker(label="End date", width=150)
  
  page.add(dp1, dp2, b, t)
  input()