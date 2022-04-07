import pglet
from pglet import Text, Textbox

with pglet.page("textbox-with-change-event") as page:

    def textbox_changed(e):
        t.value = e.control.value
        page.update()

    t = Text()
    tb = Textbox(
        label="Textbox with 'change' event:",
        on_change=textbox_changed,
    )

    page.add(tb, t)
    input()
