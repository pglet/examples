import pglet
from pglet import Message
with pglet.page("basic-messages") as page:
    page.add(
      Message(value='This is just a message.'),
      Message(value='Success message with dismiss button', dismiss=True, type='success'),
      Message(value='Error message with dismiss button', dismiss=True, type='error'))