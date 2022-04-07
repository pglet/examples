from datetime import datetime
import pglet
from pglet import DatePicker
with pglet.page("datepicker-allow-text-input") as page:
  now = datetime.now()
  page.add(
    DatePicker(width=150, label="Allow text input", allow_text_input=True),
    DatePicker(label="Allow text input with placeholder", placeholder='Select date...', allow_text_input=True, width='25%'),
    DatePicker(value=now, label="Required", required=True, allow_text_input=True))