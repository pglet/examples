import pglet
from pglet import Spinner, Text

with pglet.page("spinner-label-positioning") as page:

    page.add(
        Text("Spinner label positioning", size="xLarge"),
        Text("Spinner with label positioned below"),
        Spinner("I am definitely loading...", label_position="bottom"),
        Text("Spinner with label positioned above"),
        Spinner("Seriously, still loading...", label_position="top"),
        Text("Spinner with label positioned to right"),
        Spinner("Wait, wait...", label_position="right"),
        Text("Spinner with label positioned to left"),
        Spinner("Nope, still loading...", label_position="left"),
    )
