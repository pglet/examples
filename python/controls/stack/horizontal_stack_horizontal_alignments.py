import pglet
from pglet import Stack, Text

with pglet.page("horizontal-stack-horizontal-alignments") as page:

    bg_color = "#ddddee"
    page.horizontal_align = "stretch"

    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                Text(
                    value=i,
                    align="center",
                    vertical_align="center",
                    width=30,
                    height=30,
                    bgcolor="BlueMagenta10",
                    color="white",
                    padding=5,
                )
            )
        return items

    def horizontal_stack(horiz_align):
        return Stack(
            controls=[
                Text(value=horiz_align),
                Stack(
                    horizontal=True,
                    horizontal_align=horiz_align,
                    vertical_align="center",
                    gap=20,
                    bgcolor=bg_color,
                    controls=items(3),
                ),
            ]
        )

    page.add(
        horizontal_stack("start"),
        horizontal_stack("center"),
        horizontal_stack("center"),
        horizontal_stack("space-between"),
        horizontal_stack("space-around"),
        horizontal_stack("space-evenly"),
    )

    input()
