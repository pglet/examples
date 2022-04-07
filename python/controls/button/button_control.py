import pglet
from pglet import Button, Stack, Text, button


def buttons():
    return Stack(
        gap=20,
        controls=[
            Text("Regular buttons", size="xLarge"),
            regular_buttons(),
            Text("Compound buttons", size="xLarge"),
            compound_buttons(),
            Text("Icon buttons", size="xLarge"),
            buttons_with_icon(),
            Text("Toolbar buttons", size="xLarge"),
            toolbar_buttons(),
            Text("Icon only buttons", size="xLarge"),
            icon_only_buttons(),
            Text("Link buttons", size="xLarge"),
            link_buttons(),
            Text("Context menu buttons", size="xLarge"),
            context_menu_buttons(),
            Text("Split buttons", size="xLarge"),
            split_buttons(),
        ],
    )


def regular_buttons():
    return Stack(
        controls=[
            Stack(
                horizontal=True,
                controls=[
                    Button("Standard"),
                    Button("Standard disabled", disabled=True),
                ],
            ),
            Stack(
                horizontal=True,
                controls=[
                    Button("Primary", primary=True),
                    Button("Primary disabled", primary=True, disabled=True),
                ],
            ),
            Stack(horizontal=True, controls=[button_with_on_click()]),
        ]
    )


def button_with_on_click():
    def button_clicked(e):
        # print(e)
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        stack.update()

    b = Button(
        "Button with on_click event", on_click=button_clicked, title="Click me!", data=0
    )
    t = Text()
    stack = Stack(controls=[b, t])
    return stack


def compound_buttons():
    return Stack(
        horizontal=True,
        controls=[
            Button(
                "Compound", secondary_text="This is a secondary text", compound=True
            ),
            Button(
                "Primary compound",
                secondary_text="This is a secondary text",
                compound=True,
                primary=True,
            ),
        ],
    )


def buttons_with_icon():
    return Stack(
        horizontal=True,
        controls=[
            Button("Create account", icon="AddFriend", primary=True),
            Button("New item", icon="Add"),
            Button("Delete", icon="Delete"),
        ],
    )


def toolbar_buttons():
    return Stack(
        horizontal=True,
        controls=[
            Button(text="New item", toolbar=True, icon="Add"),
            Button(text="Send", toolbar=True, icon="Mail"),
            Button(text="Show example", toolbar=True, icon="ChevronDown"),
            Button(text="Delete", toolbar=True, icon_color="red", icon="Delete"),
        ],
    )


def icon_only_buttons():
    return Stack(
        horizontal=True,
        controls=[
            Button(icon="Emoji2", title="Emoji!"),
            Button(icon="Calendar", title="Calendar!"),
        ],
    )


def link_buttons():
    return Stack(
        horizontal=True,
        controls=[
            Button(
                action=True,
                icon="Globe",
                text="Pglet website",
                url="https://pglet.io",
                new_window=True,
            ),
            Button(
                icon="MyMoviesTV",
                text="Go to Disney",
                url="https://disney.com",
                new_window=True,
            ),
        ],
    )


def context_menu_buttons():
    return Stack(
        horizontal=True,
        controls=[
            Button(
                icon="Add",
                text="New item",
                menu_items=[
                    button.MenuItem(text="Email message", icon="Mail"),
                    button.MenuItem(text="Calendar event", icon="Calendar"),
                ],
            ),
            Button(
                text="Button with sub-menus",
                menu_items=[
                    button.MenuItem(
                        text="New",
                        icon="Add",
                        sub_menu_items=[
                            button.MenuItem(text="Email message", icon="Mail"),
                            button.MenuItem(text="Calendar event", icon="Calendar"),
                        ],
                    ),
                    button.MenuItem(
                        text="Share",
                        icon="Share",
                        split=True,
                        sub_menu_items=[
                            button.MenuItem(text="Share to Twitter"),
                            button.MenuItem(text="Share to Facebook"),
                            button.MenuItem("Share to Somewhere"),
                            button.MenuItem(
                                "Share to email",
                                sub_menu_items=[
                                    button.MenuItem("Share to Outlook"),
                                    button.MenuItem("Share to Gmail"),
                                ],
                            ),
                        ],
                    ),
                    button.MenuItem(divider=True),
                    button.MenuItem(
                        text="To Pglet",
                        icon="Globe",
                        icon_color="green",
                        url="https://pglet.io",
                        new_window=True,
                        secondary_text="New Window",
                    ),
                ],
            ),
        ],
    )


def split_buttons():
    return Stack(
        horizontal=True,
        controls=[
            Button(
                split=True,
                text="Standard",
                menu_items=[
                    button.MenuItem("Email message", icon="Mail"),
                    button.MenuItem("Calendar event", icon="Calendar"),
                ],
            ),
            Button(
                split=True,
                primary=True,
                text="Primary",
                menu_items=[
                    button.MenuItem("Email message", icon="Mail"),
                    button.MenuItem("Calendar event", icon="Calendar"),
                ],
            ),
        ],
    )


def action_buttons():
    return Stack(
        horizontal=True,
        controls=[
            Button(action=True, text="<"),
            Button(action=True, text="<<"),
            Button(action=True, text=">"),
            Button(action=True, text=">>"),
        ],
    )


def main(page):

    page.title = "Button control samples"
    page.update()

    page.add(buttons())


pglet.app("python-button", target=main)
