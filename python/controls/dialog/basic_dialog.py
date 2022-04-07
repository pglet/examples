import pglet
from pglet import Button, Checkbox, Dialog, Text

with pglet.page("basic-dialog") as page:

    def button_clicked(e):
        d.open = True
        page.update()

    b = Button(text="Open dialog", on_click=button_clicked)
    page.add(b)

    d = Dialog(
        title="Welcome!",
        width=200,
        height=100,
        controls=[Text(size="small", align="center", value="This is a basic dialog")],
        footer=[Button("OK"), Button("Cancel")],
    )

    page.add(d)

    input()
