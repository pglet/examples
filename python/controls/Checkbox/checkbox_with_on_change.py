import pglet
from pglet import Checkbox

with pglet.page("myapp") as page:
    page.clean()
    from pglet import Text
    def checkbox_changed(e):
        t.value = f"Checkbox value changed to {c.value}" 
        t.update()

    c = Checkbox('Checkbox with on_change event', on_change=checkbox_changed)
    t = Text()

    page.add(c, t)

    input()