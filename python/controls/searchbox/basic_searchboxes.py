import pglet
from pglet import SearchBox
with pglet.page("basic-searchboxes") as page:
  page.add(
    SearchBox(),
    SearchBox(underlined=True, placeholder='Underlined SearchBox'),
    SearchBox(disabled=True, placeholder='Disabled SearchBox'),
    SearchBox(placeholder='SearchBox with icon', icon='Filter', icon_color='red'))