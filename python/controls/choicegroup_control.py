import pglet
from pglet import Stack, Text, ChoiceGroup, Textbox, Button
from pglet import choicegroup


def choicegroups():
    return Stack(
        gap=20,
        controls=[
            Stack(
                controls=[Text("Basic ChoiceGroup", size="xLarge"), basic_choicegroup()]
            ),
            Stack(
                controls=[
                    Text("ChoiceGroup with icons", size="xLarge"),
                    choicegroup_with_icons(),
                ]
            ),
            Stack(
                controls=[
                    Text("ChoiceGroup with on_change event", size="xLarge"),
                    choicegroup_with_on_change(),
                ]
            ),
            Stack(
                controls=[
                    Text("Change items in choicegroup options", size="xLarge"),
                    change_items_in_choicegroup(),
                ]
            ),
        ],
    )


def basic_choicegroup():
    return ChoiceGroup(
        label="Select color",
        options=[
            choicegroup.Option("Red"),
            choicegroup.Option("Green"),
            choicegroup.Option("Blue"),
        ],
    )


def choicegroup_with_icons():
    return ChoiceGroup(
        label="Pick one icon",
        options=[
            choicegroup.Option(key="day", text="Day", icon="CalendarDay"),
            choicegroup.Option(key="week", text="Week", icon="CalendarWeek"),
            choicegroup.Option(key="month", text="Month", icon="Calendar"),
        ],
    )


def choicegroup_with_on_change():
    def choicegroup_changed(e):
        t.value = f"ChoiceGroup value changed to {cg.value}"
        stack.update()

    cg = ChoiceGroup(
        label="Select color",
        on_change=choicegroup_changed,
        options=[
            choicegroup.Option("Red"),
            choicegroup.Option("Green"),
            choicegroup.Option("Blue"),
        ],
    )

    t = Text()
    stack = Stack(controls=[cg, t])
    return stack


def change_items_in_choicegroup():
    def add_clicked(e):
        cg.options.append(choicegroup.Option(new_option.value))
        new_option.value = ""
        stack.update()

    cg = ChoiceGroup()
    new_option = Textbox(placeholder="Enter new item name")
    add = Button("Add", on_click=add_clicked)
    stack = Stack(controls=[cg, Stack(horizontal=True, controls=[new_option, add])])
    return stack


def main(page):

    page.title = "ChoiceGroup control samples"
    page.update()

    page.add(choicegroups())


pglet.app("python-choicegroup", target=main)
