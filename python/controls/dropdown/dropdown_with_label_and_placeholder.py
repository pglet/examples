import pglet
from pglet import Dropdown, dropdown
with pglet.page("dropdown-with-label-and-placeholder") as page:
  page.add(Dropdown(label='Color', placeholder='What\'s your favourite color?', options=[
    dropdown.Option('Red'),
    dropdown.Option('Green'),
    dropdown.Option('Blue')
  ]))

