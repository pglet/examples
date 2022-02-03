import pglet
from pglet import Button
with pglet.page("compound-buttons") as page:
    page.add(
      Button("Compound", secondary_text='This is a secondary text', compound=True),
      Button("Primary compound", secondary_text='This is a secondary text', compound=True, primary=True))