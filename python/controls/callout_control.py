import pglet
from pglet import Stack, Text, Callout, Button, ChoiceGroup, Message
from pglet import choicegroup 

def callouts(page):

  message = Message(dismiss=True, visible=False)

  def callout_dismissed(e):
    message.value = f'Callout "{e.control.id}" dismissed'
    message.visible = True
    page.update() 

  callout1 = Callout(id='callout1', target='showCallout1', focus=True, visible=False, on_dismiss=callout_dismissed, controls=[
      Stack(padding=20, width=300, controls=[
        Text(value='Choose your style', size='xlarge'),
        ChoiceGroup(options=[
           choicegroup.Option('red'),
           choicegroup.Option('green'),
           choicegroup.Option('blue')]),
        Stack(horizontal=True, controls=[
          Button(id='yes', primary=True, text='Yes'),
          Button(id='no', text='No')
        ])      
      ])
  ])

  callout2 = Callout(id='callout2', target='showCallout2', beak=True, cover=False, position='rightTop', page_padding=0, visible=False, on_dismiss=callout_dismissed, controls=[
      Stack(padding=20, width=300, height=100, controls=[
        Text(value='That\'s a button callout!', size='xLarge')
      ])
  ])
  
  def button_clicked(e):
    if e.control.id=='showCallout1':
      callout1.visible = True
    elif e.control.id=='showCallout2':
      callout2.visible = True
    page.update()



  return Stack(controls=[
      message,
      Stack(horizontal=True, controls=[
          Button(id='showCallout1', text='Show bottom callout', on_click=button_clicked),
          Button(id='showCallout2', text='Show right callout', on_click=button_clicked)
        ]),
      callout1,
      callout2
    ])

def main(page):
    
  page.title = "Callout control samples"
  page.update()
  page.add(callouts(page))

pglet.app("callout-control-samples", target = main)

input("Press Enter to exit...")