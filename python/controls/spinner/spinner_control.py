import pglet
from pglet import Spinner, Text


def main(page):
    page.add(
        Text("Spinner sizes", size="xLarge"),
        Spinner("Extra small spinner", size="xSmall", label_position="left"),
        Spinner("Small spinner", size="small", label_position="left"),
        Spinner("Medium spinner", size="medium", label_position="left"),
        Spinner("Large spinner", size="large", label_position="left"),
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


pglet.app("python-spinner", target=main)
