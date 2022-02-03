import pglet
from pglet import Button
with pglet.page("link-buttons") as page:
  page.add(
    Button(action=True, icon='Globe', text='Pglet website',url='https://pglet.io', new_window=True),
    Button(icon='MyMoviesTV', text='Go to Disney', url='https://disney.com', new_window=True))