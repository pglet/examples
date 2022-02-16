import pglet
from pglet import Button, Panel, Text

with pglet.page("basic-panel") as page:

    def button_clicked(e):
        p.open = True
        page.update()

    b = Button(text="Open panel", on_click=button_clicked)
    page.add(b)

    p = Panel(title="Basic panel", controls=[Text(value="Content goes here")])

    page.add(p)

    input()
