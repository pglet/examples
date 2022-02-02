import pglet
from pglet import Stack, Text, Dropdown, Textbox, Button
from pglet import dropdown


def dropdowns():
    return Stack(
        gap=20,
        controls=[
            Stack(controls=[Text("Basic dropdown", size="xLarge"), basic_dropdown()]),
            Stack(
                controls=[
                    Text("Dropdown with label and placeholder", size="xLarge"),
                    dropdown_with_label_and_placeholder(),
                ]
            ),
            Stack(
                controls=[
                    Text("Dropdown with on_change event", size="xLarge"),
                    dropdown_with_on_change(),
                ]
            ),
            Stack(
                controls=[
                    Text("Change items in dropdown options", size="xLarge"),
                    change_items_in_dropdown(),
                ]
            ),
        ],
    )


def basic_dropdown():
    return Dropdown(
        options=[
            dropdown.Option("Red"),
            dropdown.Option("Green"),
            dropdown.Option("Blue"),
        ]
    )


def dropdown_with_label_and_placeholder():
    return Dropdown(
        label="Color",
        placeholder="What's your favourite color?",
        options=[
            dropdown.Option("Red"),
            dropdown.Option("Green"),
            dropdown.Option("Blue"),
        ],
    )


def dropdown_with_on_change():
    def dropdown_changed(e):
        t.value = f"Dropdown changed to {d.value}"
        stack.update()

    d = Dropdown(
        on_change=dropdown_changed,
        options=[
            dropdown.Option("Red"),
            dropdown.Option("Green"),
            dropdown.Option("Blue"),
        ],
    )

    t = Text()
    stack = Stack(controls=[d, t])
    return stack


def change_items_in_dropdown():
    def add_clicked(e):
        d.options.append(dropdown.Option(new_option.value))
        d.value = new_option.value
        new_option.value = ""
        stack.update()

    d = Dropdown()
    new_option = Textbox(placeholder="Enter new item name")
    add = Button("Add", on_click=add_clicked)
    stack = Stack(controls=[d, Stack(horizontal=True, controls=[new_option, add])])
    return stack


def main(page):

    page.title = "Dropdown control samples"
    page.update()

    page.add(dropdowns())


pglet.app("python-dropdown", target=main)
