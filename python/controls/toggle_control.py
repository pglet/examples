import pglet
from pglet import Stack, Text, Toggle

'''

  pglet_send "add
    toggle label='Enabled and checked' value='true'
    toggle label='Enabled and unchecked'
    toggle disabled label='Disabled and checked' value='true'
    toggle disabled label='Disabled and unchecked'
    toggle inline label='With inline label' onText=On offText=Off
    toggle disabled inline label='Disabled with inline label' onText=On offText=Off
    toggle inline label='With inline label and without onText and offText'
    toggle disabled inline label='Disabled with inline label and without onText and offText'  
  "
'''

def toggles(page):
  return Stack(controls=[
        Text("Toggles", size="xLarge"),
        Toggle(label='Enabled and checked', value=True),
        Toggle(label='Enabled and unchecked'),
        Toggle(disabled=True, label='Disabled and checked', value=True),
        Toggle(disabled=True, label='Disabled and unchecked'),
        Toggle(inline=True, label='With inline label', on_text='On', off_text='Off'),
        Toggle(disabled=True, inline=True, label='Disabled with inline label', on_text='On', off_text='Off'),
        Toggle(inline=True, label='With inline label and without onText and offText'),
        Toggle(disabled=True, inline=True, label='Disabled with inline label and without onText and offText'),
        toggle_with_on_change(page=page)
        ])

def toggle_with_on_change(page):
    
    def toggle_changed(e):
      if t.value:
        # Dark theme
        page.theme_background_color = '#262626'
        page.theme_primary_color = '#3ee66d'
        page.theme_text_color='#edd2b7'
      else:
        #page.horizontal_align = 'stretch'
        page.theme_background_color = ''
        page.theme_primary_color = ''
        page.theme_text_color=''
      
      page.update()

    t = Toggle(label="With Change event", on_text="Dark theme", off_text="Light theme", value=False, on_change=toggle_changed)
    return t

def main(page):
    
    page.title = "Toggle control samples"
    page.update()
    page.add(toggles(page))

pglet.app("toggle-control-samples", target = main)

input("Press Enter to exit...") 