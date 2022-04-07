import pglet
from pglet import Text

page = pglet.page(web=True)
page.title = "Hello, world!"
page.add(Text("Hello, world!"))
