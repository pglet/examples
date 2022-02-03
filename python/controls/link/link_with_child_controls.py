import pglet
from pglet import Link
with pglet.page("myapp") as page:
    page.clean()
    from pglet import Text, Icon, Button
    page.add(
        Link(url='http://google.com', controls=[
        Icon('Globe'),
        Button('Action Button', action = True),
        Text(' Link with child controls')
    ]))