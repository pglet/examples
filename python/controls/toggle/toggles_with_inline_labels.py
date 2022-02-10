import pglet
from pglet import Toggle

with pglet.page("toggles-with-inline-labels") as page:

    page.add(
        Toggle(inline=True, label="With inline label", on_text="On", off_text="Off"),
        Toggle(
            disabled=True,
            inline=True,
            label="Disabled with inline label",
            on_text="On",
            off_text="Off",
        ),
        Toggle(inline=True, label="With inline label and without onText and offText"),
        Toggle(
            disabled=True,
            inline=True,
            label="Disabled with inline label and without onText and offText",
        ),
    )
