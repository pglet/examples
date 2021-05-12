import pglet
from pglet import Stack, Text, Slider

page = pglet.page()

def slider_with_on_change():
    
    def slider_changed(e):
      s.data += 1
      t.value = f"Slider changed to {int(s.value)}"
      stack.update()

    s = Slider('Change the slider to trigger Change event', on_change=slider_changed, data=0)
    t = Text()
    stack = Stack(controls=[s, t])
    return stack

stack = Stack(width='50%', controls=[
        Text("Slider with Change event", size="xLarge"),
        slider_with_on_change()
])

page.add(stack)

input("Press Enter to exit...")