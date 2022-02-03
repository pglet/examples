import pglet
from pglet import Link
with pglet.page("basic-links") as page:
    page.add(
        Link(url='http://google.com', value='Visit Google', new_window=True),
        Link(value='Link without URL', size='large'),
        Link(url='http://google.com', value='Disabled link', disabled=True))