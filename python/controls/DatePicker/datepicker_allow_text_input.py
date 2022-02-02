from datetime import datetime
import pglet
from pglet import DatePicker
with pglet.page("myapp") as page:
  page.clean()
  now = datetime.now()
  page.add(
      DatePicker(width=150, label="Allow text input", allow_text_input=True))