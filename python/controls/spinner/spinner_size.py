import pglet
from pglet import Spinner, Text

with pglet.page("spinner-size") as page:

    page.add(
        Text("Spinner sizes", size="xLarge"),
        Spinner("Extra small spinner", size="xSmall", label_position="left"),
        Spinner("Small spinner", size="small", label_position="left"),
        Spinner("Medium spinner", size="medium", label_position="left"),
        Spinner("Large spinner", size="large", label_position="left"),
    )
