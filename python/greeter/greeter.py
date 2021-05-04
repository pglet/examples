import sys
import pglet
from pglet import Textbox, Button, Text

p = pglet.page("greeter")
p.clean()

def say_hello_click(e):
    name = p.get_value(txt_name)
    p.clean()
    p.add(Text(value=f'Hello, {name}!'))
    sys.exit()

txt_name = p.add(Textbox(label="Your name", description="Please provide your full name"), Textbox(label="Your name", description="Please provide your full name"))
print("txt_name ", txt_name)
p.add(Button(text="Say hello", primary=True, onclick=say_hello_click))

# wait until browser window is closed or page reloaded
p.wait_close()