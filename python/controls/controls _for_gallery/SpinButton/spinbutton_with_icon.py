import pglet
from pglet import Stack, Text, SpinButton

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Spinbutton with icon", size="xLarge"),
        SpinButton(icon='IncreaseIndentLegacy', label='SpinButton with icon:', min=0, max=100, step=1, value=0)
    ])

page.add(stack)