import pglet
from pglet import Button, Panel, Text

with pglet.page("panel-custom") as page:

    def button_clicked(e):
        p.open = True
        page.update()

    b = Button(text="Open panel", on_click=button_clicked)
    page.add(b)

    p = Panel(
        title="Panel with autoDimiss = True",
        auto_dismiss=False,
        controls=[Text(value="Click anywhere outside the panel to close it")],
    )

    page.add(p)

    input()
