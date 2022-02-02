from datetime import datetime
import pglet
from pglet import DatePicker
with pglet.page("myapp") as page:
  page.clean()
  now = datetime.now()
  page.add(
      DatePicker(label="Start date", value=now, width=150),
      DatePicker(label="End date", width=150))