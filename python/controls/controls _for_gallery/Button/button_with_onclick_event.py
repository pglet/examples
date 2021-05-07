import pglet
from pglet import Stack, Text, Button

page = pglet.page()

def button_with_on_click():
    
    def button_clicked(e):
      b.data += 1
      t.value = f"Button clicked {b.data} time(s)"
      stack.update()

    b = Button('Button', on_click=button_clicked, title='Click me!', data=0)
    t = Text()
    stack = Stack(controls=[b, t])
    return stack

stack = Stack(controls=[
    Text('Button with on_click event', size='xLarge'),
    button_with_on_click()
])

page.add(stack)

input("Press Enter to exit...")