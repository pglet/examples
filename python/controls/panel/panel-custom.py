import pglet
from pglet import Button, Dropdown, Panel, Text, Textbox, dropdown

with pglet.page("panel-custom") as page:

    def button_clicked(e):
        p.type = dd.value
        p.width = tb.value
        tb.value = ""
        p.open = True
        page.update()

    dd = Dropdown(
        width=100,
        value="custom",
        options=[
            dropdown.Option("custom"),
            dropdown.Option("customLeft"),
        ],
    )
    b = Button(text="Open panel", on_click=button_clicked)
    tb = Textbox(label="Width", placeholder="For example, 888px, 888 or 50%", width=500)
    page.add(dd, tb, b)

    p = Panel(title="Basic panel", controls=[Text(value="Content goes here")])

    page.add(p)

    input()
