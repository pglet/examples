import pglet
from pglet import Textbox
with pglet.page("password-with-reveal-button") as page:

  page.add(Textbox(label='Password with reveal button', password=True))
  
