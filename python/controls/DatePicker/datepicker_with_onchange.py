from datetime import datetime
import pglet
from pglet import DatePicker
with pglet.page("myapp") as page:
  page.clean()
  from pglet import Text
  def datepicker_changed(e):
        t.value = f"DatePicker value changed to {dp.value}" 
        t.update()

  now = datetime.now()
  t = Text()
  dp = DatePicker(label="Start date", value=now, width=150, on_change=datepicker_changed)
  
  page.add(dp, t)
  input()