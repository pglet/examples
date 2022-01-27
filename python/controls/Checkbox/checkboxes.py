import pglet
from pglet import Checkbox
with pglet.page("myapp") as page:
  page.clean()
  page.add(
    Checkbox(label='Unchecked checkbox', value=False),
    Checkbox(label='Checked checkbox', value=True),
    Checkbox(label='Disabled checkbox', disabled=True),
    Checkbox(label="Checkbox with rendered box_side='End'", box_side='End'))
