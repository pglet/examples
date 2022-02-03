import pglet
from pglet import Stack, Button, Textbox, Text, Dialog

pub_sub = {}


def broadcast(user, message):
    for session_id, handler in pub_sub.items():
        handler(user, message)


def main(page):

    messages = Stack()
    message = Textbox()

    def on_message(user, message):
        messages.controls.append(Text(f"{user}: {message}"))
        page.update()

    pub_sub[page.session_id] = on_message

    def send_click(e):
        broadcast(page.session_id, message.value)
        message.value = ""
        page.update()

    send = Button("Send", on_click=send_click)
    form = Stack(horizontal=True, controls=[message, send])
    page.add(messages, form)


pglet.app("feodor/chat", target=main)
