import pglet
from pglet import Message
with pglet.page("myapp") as page:
    page.clean()
    from pglet import Text
    def message_dismissed(e):
      t.value = "Message dismissed!"
      page.update()

    m = Message(value='Message with dismiss event', dismiss=True, on_dismiss=message_dismissed)
    t = Text()
  
    page.add(m, t)
    input()