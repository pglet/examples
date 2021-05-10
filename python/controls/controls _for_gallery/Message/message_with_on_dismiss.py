import pglet
from pglet import Stack, Text, Message, MessageButton

page = pglet.page()

def message_with_on_dismiss():

  def message_dismissed(e):
    t.value = "Message dismissed!"
    stack.update()

  m = Message(value='Click on the X button', dismiss=True, on_dismiss=message_dismissed)
  t = Text()
  stack = Stack(controls=[m, t])
  return stack

stack = Stack(width='70%', gap=20, controls=[
    Text('Message with on_dismiss event', size='xLarge'),
    message_with_on_dismiss()
    ])

page.add(stack)

input("Press Enter to exit...")