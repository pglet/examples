import pglet
import time
from pglet import Textbox, Button, Text, Progress, Stack

page = pglet.page()

txt = Textbox(label="Your name")
btn = Button(text="Say hello", primary=True)
page.add(txt, btn)

while True:
    e = page.wait_event()

    if e.target == btn.id and e.name == "clicked":
        name = page.get_value(txt)

        if name == "":
            txt.error_message = "Name cannot be blank"
            btn.text = "Say it again!"
            page.update(txt, btn)
            continue

        page.remove(btn)
        page.add(Text(value=f'Hello, {name}!'), at=0)

        prg = page.add(Progress(label="Doing something..."))
        for i in range(1, 11):
            page.set_value(prg, i * 10)
            time.sleep(1)

        break