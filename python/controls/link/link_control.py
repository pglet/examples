import pglet
from pglet import Stack, Text, Link, Icon


def links():
    return Stack(
        gap=20,
        controls=[
            Text("Links", size="xLarge"),
            Link(url="http://google.com", value="Visit Google", new_window=True),
            Link(value="Link without URL", size="large"),
            Link(url="http://google.com", value="Disabled link", disabled=True),
            Link(
                url="http://google.com",
                controls=[Icon("Globe"), Text(" Link with child controls")],
            ),
            link_with_on_click(),
        ],
    )


def link_with_on_click():
    def link_clicked(e):
        l.data += 1
        t.value = f"Link clicked {l.data} time(s)"
        stack.update()

        # l = Link('Link with on_click event', on_click=link_clicked, title='Click me!', data=0)

    l = Link(
        value="Link with on_click event",
        on_click=link_clicked,
        title="Click me!",
        data=0,
    )
    t = Text()
    stack = Stack(controls=[l, t])
    return stack


def main(page):

    page.title = "Link control samples"
    page.update()
    page.add(links())


pglet.app("python-link", target=main)
