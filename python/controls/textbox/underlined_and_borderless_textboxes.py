import pglet
from pglet import Textbox
with pglet.page("underlined-and-borderless-textboxes") as page:

  page.add(
    Textbox(label='Underlined', underlined=True, placeholder='Enter text here'),
    Textbox(label='Borderless', borderless=True, placeholder='Enter text here'))
  
  
