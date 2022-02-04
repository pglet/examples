import pglet
from pglet import Textbox, Button
with pglet.page("textbox-with-change-event") as page:
  def textbox_changed(e):
    if tb.value =='':
        tb.error_message = 'Field is required'
    else:
        tb.error_message = ''

    page.update()

  tb = Textbox(label='Required:', required=True, on_change=textbox_changed, error_message='Field is required')

  page.add(tb)
  input()
  
