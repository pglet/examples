import pglet
from pglet import Column, Grid, Stack, Text


class Person:
    def __init__(
        self, first_name: str, last_name: str, age: int = None, employee: bool = False
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.employee = employee


with pglet.page("basic-grid") as page:

    page.add(
        Text("Basic grid", size="large"),
        Stack(
            width="50%",
            controls=[
                Grid(
                    columns=[
                        Column(name="First name", field_name="first_name"),
                        Column(name="Last name", field_name="last_name"),
                        Column(name="Age", field_name="age"),
                    ],
                    items=[
                        Person(first_name="John", last_name="Smith", age=30),
                        Person(first_name="Samantha", last_name="Fox", age=43),
                        Person(first_name="Alice", last_name="Brown", age=25),
                    ],
                )
            ],
        ),
    )
