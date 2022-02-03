from turtle import onclick
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
        broadcast(page.user, message.value)
        message.value = ""
        page.update()

    user_name = Textbox(label="Enter your name")

    page.user = page.session_id

    def join_click(e):
        if not user_name.value:
            user_name.error_message = "Name cannot be blank!"
            user_name.update()
        else:
            page.user = user_name.value
            dlg.open = False
            page.update()

    dlg = Dialog(
        open=True,
        blocking=True,
        auto_dismiss=False,
        title="Welcome!",
        controls=[user_name],
        footer=[Button(text="Join chat", primary=True, on_click=join_click)],
    )

    send = Button("Send", on_click=send_click)
    form = Stack(horizontal=True, controls=[message, send])
    page.add(messages, form, dlg)


pglet.app("feodor/chat", target=main)
