import pglet
from pglet import Stack, Text, SpinButton

def spinbuttons():
  return Stack(width='50%', controls=[
        Text("SpinButons", size="xLarge"),
        SpinButton(label='Default slider')
    ])

def main(page):

    page.title = "Spinbutton control samples"
    page.update()
    page.add(spinbuttons())

pglet.app("spinbuttons-control-samples", target = main)

input("Press Enter to exit...") 