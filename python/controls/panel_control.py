import pglet
from pglet import Stack, Text, Button, Panel, Toggle, ChoiceGroup
from pglet import choicegroup 

def panels(page):

  #light_dismiss = Toggle(label='Light dismiss', on_text='True', off_text='False', value=False)
  #modal = Toggle(label='Modal', on_text='True', off_text='False', value=False)
  panel_type = ChoiceGroup(label='Choose a panel type:', options=[
      choicegroup.Option(key='modal', text='Modal'),
      choicegroup.Option(key='modal_light_dismiss', text='Modal with light dismiss'),
      choicegroup.Option(key='non_modal', text='Non-modal'),
  ])

  panel_size = ChoiceGroup(label='Choose a panel size:', options=[
      choicegroup.Option(key='Small', text='Small'),
      choicegroup.Option(key='smallLeft', text='Small, near side'),
      choicegroup.Option(key='Medium', text='Medium'),
  ])

  light_dismiss_text = Text(visible=False, value='This panel uses "light dismiss" behavior: it can be closed by clicking or tapping the area outside the panel (or using the close button as usual).')
  non_modal_text = Text(visible=False, value="This panel is non-modal: even when it's open, it allows interacting with content outside the panel.")

  def panel_dismissed(e):
    light_dismiss_text.visible = False
    non_modal_text.visible = False
    page.update()

  panel = Panel(title='Panel', on_dismiss=panel_dismissed, controls=[
      light_dismiss_text,
      non_modal_text
  ], footer=[
        Button(text='Yes'),
        Button(text='No')
    ])
    
  def button_clicked(e):
    if panel_type.value == 'modal':
        panel.light_dismiss = False
        panel.blocking = True
    elif panel_type.value == 'modal_light_dismiss':
        panel.light_dismiss = True
        panel.blocking = True
    elif panel_type.value == 'non_modal':
        panel.light_dismiss = False
        panel.blocking = False

    panel.type = panel_size.value
    
    if panel.light_dismiss:
        light_dismiss_text.visible = True
    if panel.blocking == False:
        non_modal_text.visible = True
    
    panel.open = True
    page.update()

  return Stack(gap=30, controls=[
      Stack(horizontal_align='start', controls=[
          #Text("Choose your panel options", size="xLarge"),
          panel_type,
          panel_size,
          Button("Open panel", on_click=button_clicked),
          panel
      ])
  ])

def main(page):
    
  page.title = "Dialog control samples"
  page.update()
  page.add(panels(page))

pglet.app("panel-control-samples", target = main)

input("Press Enter to exit...")