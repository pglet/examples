import pglet
from pglet import Link, Text

with pglet.page("link-with-click-event") as page:

    def link_clicked(e):
        l.data += 1
        t.value = f"Link clicked {l.data} time(s)"
        page.update()

    l = Link(
        value="Link with 'click' event",
        on_click=link_clicked,
        title="Click me!",
        data=0,
    )
    t = Text()

    page.add(l, t)
    input()
