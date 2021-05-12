import pglet
from pglet import Stack, Text, SpinButton

page = pglet.page()

def spinbutton_with_on_change():
    
    def spinbutton_changed(e):
      s.data += 1
      t.value = f"Spinbutton changed to {int(s.value)}"
      stack.update()

    s = SpinButton('SpinButton with Change event', on_change=spinbutton_changed, data=0)
    t = Text()
    stack = Stack(controls=[s, t])
    return stack

stack = Stack(gap=20, controls=[
    Text("Spinbutton with Change event", size="xLarge"),
        spinbutton_with_on_change()
    ])

page.add(stack)

input("Press Enter to exit...")