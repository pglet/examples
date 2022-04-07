import pglet
from pglet import Checkbox, Stack, Text


def checkboxes():
    return Stack(
        gap=20,
        controls=[
            Text("Checkboxes", size="xLarge"),
            Checkbox(label="Unchecked checkbox", value=False),
            Checkbox(label="Checked checkbox", value=True),
            Checkbox(label="Disabled checkbox", disabled=True),
            Checkbox(label="Checkbox with rendered box_side='end'", box_side="end"),
            checkbox_with_on_change(),
        ],
    )


def checkbox_with_on_change():
    def checkbox_changed(e):
        t.value = f"Checkbox value changed to {c.value}"
        stack.update()

    c = Checkbox("Checkbox with on_change event", on_change=checkbox_changed)
    t = Text()
    stack = Stack(controls=[c, t])
    return stack


def main(page):

    page.title = "Checkbox control samples"
    page.update()
    page.add(checkboxes())


pglet.app("python-checkbox", target=main)
