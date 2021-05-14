import pglet
from pglet import Text, Stack, Grid, Column

class Person():
    def __init__(self, first_name: str, last_name: str, age: int = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

page = pglet.page()

# Sortable grid
stack = Stack(controls = [
        Text("Compact grid with no header and multiple selection", size='large'),
        Grid(compact=True, header_visible=False, selection_mode='multiple', preserve_selection=True, columns=[
            Column(max_width=100, field_name="first_name"),
            Column(max_width=100, field_name="last_name"),
            Column(max_width=100, field_name="age")
        ], items=[
            Person(first_name='John', last_name='Smith', age=30),
            Person(first_name='Samantha', last_name='Fox', age=43),
            Person(first_name='Alice', last_name='Brown', age=25)
        ])
])

page.add(stack)