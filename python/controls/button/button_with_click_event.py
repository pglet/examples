import pglet
from pglet import Button, Text

with pglet.page("button-with-click-event") as page:
   
    def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        page.update()

    b = Button("Button with 'click' event", on_click=button_clicked, title='Click me!', data=0)
    t = Text()

    page.add(b, t)

    input()