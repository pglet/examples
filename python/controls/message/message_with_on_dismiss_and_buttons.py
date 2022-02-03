import pglet
from pglet import Message
with pglet.page("myapp") as page:
    page.clean()
    from pglet import Text, MessageButton
    def message_dismissed(e):
      t.value = f"Message dismissed with {e.data} action"
      page.update()

    m = Message(value='Message with dismiss event and buttons', dismiss=True, on_dismiss=message_dismissed, buttons=[
      MessageButton('OK'),
      MessageButton('Cancel')
  ])
    t = Text()
  
    page.add(m, t)
    input()