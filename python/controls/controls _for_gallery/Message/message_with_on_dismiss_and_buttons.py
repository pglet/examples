import pglet
from pglet import Stack, Text, Message, MessageButton

page = pglet.page()

def message_with_on_dismiss_and_buttons():

  def message_dismissed(e):
    if e.data!='':
        t.value = f"Message dismissed with {e.data} button"
    else:
        t.value = "Message dismissed with X button"
    stack.update()

  m = Message(value='Click on the X, OK or Cancel button', dismiss=True, on_dismiss=message_dismissed, buttons=[
      MessageButton('OK'),
      MessageButton('Cancel')
  ])
  t = Text()
  stack = Stack(controls=[m, t])
  return stack

stack = Stack(width='70%', gap=20, controls=[
    Text('Message with on_dismiss event and buttons', size='xLarge'),
    message_with_on_dismiss_and_buttons()
    ])

page.add(stack)

input("Press Enter to exit...")