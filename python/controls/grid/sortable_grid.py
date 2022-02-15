import pglet
from pglet import Column, Grid, Text


class Person:
    def __init__(
        self, first_name: str, last_name: str, age: int = None, employee: bool = False
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.employee = employee


with pglet.page("sortable-grid") as page:

    page.add(
        Text("Sortable grid with resizable columns and selectable rows", size="large"),
        Grid(
            selection_mode="single",
            preserve_selection=True,
            columns=[
                Column(
                    resizable=True,
                    sortable="string",
                    name="First name",
                    field_name="first_name",
                ),
                Column(
                    resizable=True,
                    sortable="string",
                    sorted="asc",
                    name="Last name",
                    field_name="last_name",
                ),
                Column(resizable=True, sortable="number", name="Age", field_name="age"),
            ],
            items=[
                Person(first_name="John", last_name="Smith", age=30),
                Person(first_name="Samantha", last_name="Fox", age=43),
                Person(first_name="Alice", last_name="Brown", age=25),
            ],
        ),
    )
