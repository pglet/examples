import pglet
from pglet import Button, Dropdown, Panel, Text, dropdown

with pglet.page("panel-size") as page:

    def button_clicked(e):
        p.type = dd.value
        p.open = True
        page.update()

    dd = Dropdown(
        width=100,
        value="small",
        options=[
            dropdown.Option("small"),
            dropdown.Option("smallLeft"),
            dropdown.Option("medium"),
            dropdown.Option("large"),
            dropdown.Option("largeFixed"),
            dropdown.Option("extraLarge"),
            dropdown.Option("fluid"),
        ],
    )
    b = Button(text="Open panel", on_click=button_clicked)
    page.add(dd, b)

    p = Panel(title="Basic panel", controls=[Text(value="Content goes here")])

    page.add(p)

    input()
