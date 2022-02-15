import pglet
from pglet import Button, Checkbox, Column, Grid, Stack, Text, Textbox, Toolbar, toolbar


class Person:
    def __init__(
        self, first_name: str, last_name: str, age: int = None, employee: bool = False
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.employee = employee


with pglet.page("dynamic-grid") as page:

    grid = None

    def delete_records(e):
        for r in grid.selected_items:
            grid.items.remove(r)
        page.update()

    delete_records = toolbar.Item(
        text="Delete records", icon="Delete", disabled=True, on_click=delete_records
    )
    grid_toolbar = Toolbar(items=[delete_records])

    def grid_items_selected(e):
        delete_records.disabled = len(e.control.selected_items) == 0
        delete_records.update()

    grid = Grid(
        selection_mode="multiple",
        compact=True,
        header_visible=True,
        columns=[
            Column(
                name="First name", template_controls=[Textbox(value="{first_name}")]
            ),
            Column(name="Last name", template_controls=[Textbox(value="{last_name}")]),
            Column(name="Age", template_controls=[Text(value="{age}")]),
            Column(
                name="Is employee", template_controls=[Checkbox(value_field="employee")]
            ),
        ],
        items=[
            Person(first_name="John", last_name="Smith", age=30, employee=False),
            Person(first_name="Jack", last_name="Brown", age=43, employee=True),
            Person(first_name="Alice", last_name="Fox", age=25, employee=False),
        ],
        margin=0,
        on_select=grid_items_selected,
    )

    first_name = Textbox("First name")
    last_name = Textbox("Last name")
    age = Textbox("Age")

    def add_record(e):
        grid.items.append(
            Person(
                first_name=first_name.value,
                last_name=last_name.value,
                age=age.value,
                employee=True,
            )
        )
        first_name.value = ""
        last_name.value = ""
        age.value = ""
        page.update()

    page.add(
        Text("Dynamic grid with template columns", size="large"),
        grid_toolbar,
        grid,
        Text("Add new employee record", size="medium"),
        Stack(horizontal=True, controls=[first_name, last_name, age]),
        Button("Add record", on_click=add_record),
    )

    input()
