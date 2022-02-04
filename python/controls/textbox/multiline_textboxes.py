import pglet
from pglet import Textbox
with pglet.page("multiline-textboxes") as page:

  page.add(
      Textbox(label='standard', multiline=True),
      Textbox(label='disabled', multiline=True, disabled=True, value='line1\nline2\nline3\nline4\nline5\n'),
      Textbox(label='With auto adjusted height', multiline=True, auto_adjust_height=True))
  
  
