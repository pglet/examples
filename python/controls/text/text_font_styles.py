import pglet
from pglet import Text
with pglet.page("text-with-different-font-styles") as page:
  
  page.add(
    Text('Bold', bold=True),
    Text('Italic', italic=True),
    Text('Preformatted text in monospace font', pre=True))
  
