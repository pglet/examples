import pglet
from pglet import Callout, Button, Text, Stack
with pglet.page("basic-callout") as page:
      
  def button_clicked(e):
        c.visible = True
        page.update()


  b = Button(text='Show callout', on_click=button_clicked)
  page.add(b)

  c = Callout(target=b.uid, width=200, height=100, visible = False, controls=[
        Stack(controls=[
          Text(size='large', align='center', value='Callout title'),
          Text(size='small', align='center', value='This is a basic callout')
      ])
  ])
  
  page.add(c)

  input()
  
  
