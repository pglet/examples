import pglet
from pglet import Textbox, Button, Text

def main(page):

    def on_click(e):
        name = page.get_value(txt_name)
        page.clean()
        page.add(Text(f"Hello, {name}!"))

    txt_name = Textbox("Your name")
    page.add(
        txt_name,
        Button("Say hello!", onclick=on_click)
    )

pglet.app(target=main, web=True)
