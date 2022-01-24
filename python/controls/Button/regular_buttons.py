import pglet
from pglet import Button
with pglet.page("myapp") as page:
    page.clean()
    page.add(
        Button("Standard"),
        Button("Standard disabled", disabled=True),
        Button("Primary", primary=True),
        Button("Primary disabled", primary=True, disabled=True))