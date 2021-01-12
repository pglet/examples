import pglet
from pglet import Textbox, Button, Text

class GreeterApp:
    def __init__(self, p):
        self.p = p
        self.main()
    
    def main(self):
        self.txt_name = self.p.add(Textbox(label="Your name", description="Please provide your full name"))
        self.p.add(Button(text="Say hello", primary=True, onclick=self.say_hello_click))

    def say_hello_click(self, e):
        name = self.p.get_value(self.txt_name)
        self.p.clean()
        self.p.add(Text(value=f'Hello, {name}!'))

pglet.app("greeter-app", target=GreeterApp)