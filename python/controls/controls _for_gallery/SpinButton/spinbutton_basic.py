import pglet
from pglet import Stack, Text, SpinButton

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Spinbuttons", size="xLarge"),
        SpinButton(label='Basic SpinButton:', min=0, max=100, step=1, value=0),
        SpinButton(disabled=True, label='Disabled SpinButton:', min=0, max=100, step=1, value=0)
    ])

page.add(stack)