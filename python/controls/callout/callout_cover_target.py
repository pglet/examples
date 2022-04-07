import pglet
from pglet import Callout, Button, Text, Stack
with pglet.page("callout-cover-target") as page:
      
  def button_clicked(e):
        c.visible = True
        page.update()


  b = Button(text='Show callout', on_click=button_clicked)
  page.add(b)

  c = Callout(target=b.uid, width=200, height=100, visible = False, cover=True, controls=[
        Stack(controls=[
          Text(size='large', align='center', value='Callout title'),
          Text(size='small', align='center', value='This callout covers target')
      ])
  ])
  
  page.add(c)

  input()
  
  
