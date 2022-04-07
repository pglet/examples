import pglet
from pglet import Link, Text, Icon, Button
with pglet.page("link-with-child-controls") as page:

    page.add(
        Link(url='http://google.com', controls=[
        Icon('Globe'),
        Button('Action Button', action = True),
        Text(' Link with child controls')
    ]))