import pglet
from pglet import Stack, Textbox, Button, Checkbox


class Task:
    def __init__(self, app, name):
        self.app = app
        self.display_task = Checkbox(value=False, label=name)
        self.edit_name = Textbox(width="100%")

        self.display_view = Stack(
            horizontal=True,
            horizontal_align="space-between",
            vertical_align="center",
            controls=[
                self.display_task,
                Stack(
                    horizontal=True,
                    gap="0",
                    controls=[
                        Button(
                            icon="Edit", title="Edit todo", on_click=self.edit_clicked
                        ),
                        Button(
                            icon="Delete",
                            title="Delete todo",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Stack(
            visible=False,
            horizontal=True,
            horizontal_align="space-between",
            vertical_align="center",
            controls=[self.edit_name, Button(text="Save", on_click=self.save_clicked)],
        )
        self.view = Stack(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.view.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.view.update()

    def delete_clicked(self, e):
        self.app.delete_task(self)


class TodoApp:
    def __init__(self):
        self.tasks = []
        self.new_task = Textbox(placeholder="Whats needs to be done?", width="100%")
        self.tasks_view = Stack()

        # application's root control (i.e. "view") containing all other controls
        self.view = Stack(
            width="70%",
            controls=[
                Stack(
                    horizontal=True,
                    on_submit=self.add_clicked,
                    controls=[self.new_task, Button("Add", on_click=self.add_clicked)],
                ),
                self.tasks_view,
            ],
        )

    def add_clicked(self, e):
        task = Task(self, self.new_task.value)
        self.tasks.append(task)
        self.tasks_view.controls.append(task.view)
        self.new_task.value = ""
        self.view.update()

    def delete_task(self, task):
        self.tasks.remove(task)
        self.tasks_view.controls.remove(task.view)
        self.view.update()


def main(page):
    page.title = "ToDo App"
    page.horizontal_align = "center"
    page.update()

    # create application instance
    app = TodoApp()

    # add application's root control to the page
    page.add(app.view)


pglet.app("todo-app", target=main)
