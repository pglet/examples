import pglet
from pglet import SplitStack, Stack, Text
from pglet.button import Button

def split_resize(e):
    for c in e.control.controls:
        print("size", c.width if e.control.horizontal else c.height)


page = pglet.page("split1")
page.title = "Split test"
page.horizontal_align = "stretch"
page.vertical_fill = True
st = SplitStack(
    height="100%",
    horizontal=True,
    # gutter_color="#eee",
    gutter_size=10,
    on_resize=split_resize,
    controls=[
        Stack(width="200", min_width="200", height="100%", controls=[Text("Column A")]),
        Stack(height="100%", controls=[Text("Column B")]),
        Stack(
            height="100%",
            width="30%",
            controls=[
                SplitStack(
                    height="100%",
                    gutter_color="yellow",
                    gutter_hover_color="orange",
                    gutter_drag_color="blue",
                    on_resize=split_resize,
                    controls=[
                        Stack(
                            width="100%",
                            bgcolor="lightGreen",
                            controls=[Text("Row A")],
                        ),
                        Stack(
                            width="100%",
                            height="200",
                            max_height="400",
                            bgcolor="lightGreen",
                            controls=[Text("Row B")],
                        ),
                    ],
                )
            ],
        ),
    ],
)
page.add(st)

input()
