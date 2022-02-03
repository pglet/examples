from datetime import datetime
import pglet
from pglet import DatePicker, Text
with pglet.page("datepicker-with-change-event") as page:
  def datepicker_changed(e):
        t.value = f"DatePicker value changed to {dp.value}" 
        t.update()

  now = datetime.now()
  t = Text()
  dp = DatePicker(label="Start date", value=now, width=150, on_change=datepicker_changed)
  
  page.add(dp, t)
  input()