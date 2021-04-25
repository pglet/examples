import pglet
from pglet import Stack, Text, Callout

def callouts(page):

  '''
  def tabs_changed(e):
    page.controls.insert(0, Message(value=f'Tabs changed to "{e.control.value}", count increased', dismiss=True))
    e.control.tabs[2].count +=1
    page.update()
  '''

'''
function main() {
  pglet_send "set page padding=0"
  pglet_send "add
stack horizontal
  button id=showCallout text='Show bottom callout'
  button id=showCallout2 text='Show right callout'
callout id=callout1 target='showCallout' focus=true visible=false
  stack padding=20 width=300
    text value='Choose your style' size=xlarge
    choicegroup
      option key=red
      option key=green
      option key=blue
    stack horizontal
      button id=yes primary text=Yes
      button id=no text=No
callout id=callout2 target='showCallout2' beak=true cover=false position=rightTop pagePadding=0 visible=false
  stack padding=20 width=300 height=100
    text value='That\'s a button callout!' size=xlarge"

  while true
  do
      pglet_wait_event
      if [[ "$PGLET_EVENT_TARGET" == "showCallout" ]]; then
        pglet_send "set callout1 visible=true"
      elif [[ "$PGLET_EVENT_TARGET" == "showCallout2" ]]; then
        pglet_send "set callout2 visible=true"
      fi
  done
}
'''
'''
  def button1_clicked(event):
    print('Button1 is clicked!')
    c.visible = True
    page.update(c)
    #page.send('set callout1 visible"True"')

  button1 = Button(id='button1', text='Click to see callout', on_click=button1_clicked)
  c = Callout(target='button1', position='leftBottom', gap=100, beak=True, beak_width=10, page_padding=10,
    focus=False, cover=True, visible=True, controls=[
        Text(value='This is callout')
        ])
'''
#page.add(button1, c)
       
  return Stack(controls=[
      Stack(horizontal=True, controls=[
          Button(id='showCallout1', text='Show bottom callout'),
          Button(id='showCallout2', text='Show right callout'),
        ]),
      callout1,
      callout2
    ])

def main(page):
    
    page.title = "Callout control samples"
    page.padding = '0'
    page.update()
    page.add(callouts(page))

pglet.app("callout-control-samples", target = main)

input("Press Enter to exit...")