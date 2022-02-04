import pglet
from pglet import Textbox, Button
with pglet.page("required-textboxes-with-error-messages") as page:
  def button_clicked(e):
    if tb1.value =='':
        tb1.error_message = 'Field is required'
    else:
        tb1.error_message = ''
    if tb2.value =='':
        tb2.error_message = 'Field is required'
    else:
        tb2.error_message = ''
    page.update()

  b = Button(text='Validate', on_click=button_clicked)
  tb1 = Textbox(label='Required:', required=True)
  tb2 = Textbox(required=True)

  page.add(tb1, tb2, b)
  input()
  
