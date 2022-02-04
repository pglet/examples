import pglet
from pglet import Textbox
with pglet.page("suffix-prefix-textboxes") as page:

  page.add(
    Textbox(label='With prefix', prefix='https://'),
    Textbox(label='With suffix', suffix='.com'),
    Textbox(label='With prefix and suffix', prefix='https://', suffix='.com'))
  
  
