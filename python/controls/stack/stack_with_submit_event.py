import pglet
from pglet import Stack, Text, Textbox, Message
with pglet.page("stack-with-submit-event") as page:

  bg_color = '#ddddee'
  page.horizontal_align = 'stretch'

  def stack_on_submit(e):
        stack = e.control
        stack.controls.insert(0, Message("Form has been submitted!", type='success', dismiss=True))
        stack.update()
  
  form1 = Stack(padding=10, width='50%', border='2px solid #eee', border_radius=5, controls=[
        Text("Pressing ENTER inside the stack will fire 'submit' event."),
        Textbox("First name"),
        Textbox("Last name")
    ], on_submit=stack_on_submit)

  page.add(form1)

  input()
  
  
