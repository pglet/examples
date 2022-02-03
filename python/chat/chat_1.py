import pglet
from pglet import Stack, Button, Textbox, Text


def main(page):
    messages = Stack()
    message = Textbox()

    def send_click(e):
        messages.controls.append(Text(message.value))
        message.value = ""
        page.update()

    send = Button("Send", on_click=send_click)
    form = Stack(horizontal=True, controls=[message, send])
    page.add(messages, form)


pglet.app("chat", target=main)
