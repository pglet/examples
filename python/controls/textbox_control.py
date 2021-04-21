import pglet
from pglet import Stack, Text, Textbox

def textboxes():
  return Stack(gap=20, controls=[
    Text("Basic textboxes", size="xLarge"),
    basic_textboxes(),
    
    Text("Multiline textboxes", size="xLarge"),
    multiline_textboxes()  
  ])

'''  

def basic_textboxes():
  return Stack(gap=20, controls=[
    Text("Standard", size="Large"),
    standard_textbox(),
    
    Text("Disabled", size="Large"),
    disabled_textbox(),

    Text("Read-only", size="Large"),
    readonly_textbox(),

    Text("Required *", size="Large"), #???
    required_textbox(),

    Text("With error message", size="Large"), #???
    with_error_message_textbox(),

    Text("With an icon", size="Large"), #???
    with_an_icon_textbox(),
    
    Text("With placeholder", size="Large"), #???
    with_placeholder_textbox(),

    Text("Password with reveal button", size="Large"), #???
    password_textbox()
  ])
'''  

'''

def multiline_textboxes():
  return Stack(gap=20, controls=[
    Text("Standard", size="Large"),
    standard_multiline_textbox(),
    
    Text("Disabled", size="Large"),
    disabled_multiline_textbox(),

    Text("Read-only", size="Large"),
    readonly_textbox(),

    Text("Non-resizable", size="Large"), #???
    nonresizable_textbox(),

    Text("With auto adjusting height", size="Large"), #???
    with_auto_adjusting_height_textbox(),

    Text("Switches from single to multiline if more than 50 characters are entered", size="Large"), #???
    switches_to_multiline_textbox()
  ])
'''

def basic_textboxes():
  return Stack(controls=[
    Stack(horizontal=True, controls=[
      Textbox(label='Standard'),
      Textbox(label='Disabled', disabled=True)
    ]),
    Stack(horizontal=True, controls=[
      Textbox(label='Read-only'), #need to add read-only property  
      Textbox(label="With placeholder", placeholder='Please enter text here')
    ]),
    Stack(horizontal=True, controls=[
      Textbox(label='Required *'), #need to add required property. How to dispay * in red?
      Textbox(label="With error message", error_message='Error message')
    ]),
    Stack(horizontal=True, controls=[
      Textbox(label='With an icon'), #need icon property
      Textbox(label='Password with reveal button', password=True)
    ]),
    Stack(horizontal=True, controls=[
      textbox_with_onchange()
    ])

  ])

def textbox_with_onchange():
    def textbox_changed(e):
        print(e)
    txt=Textbox(label='With onchange event', on_change=textbox_changed)
    return Stack(controls=[
        txt,
        Text(value=txt.value)])

    


def multiline_textboxes():
  return Stack(controls=[
    Stack(horizontal=True, controls=[
      Stack(controls=[
          Text("Standard", size="Large"),
          Textbox(multiline=True)
      ]),
      Stack(controls=[
          Text("Disabled", size="Large"),
          Textbox(multiline=True, disabled=True)
      ])
    ]),
    Stack(horizontal=True, controls=[
      Stack(controls=[
          Text("Non-resizable", size="Large"),
          Textbox()
      ]),
      Stack(controls=[
          Text("With auto adjusted height", size="Large"),
          Textbox(placeholder='Please enter text here')
      ])
    ])
  ])

def main(page):

    page.title = "Textbox control samples"
    page.update()
    #page.clean(True)

    page.add(textboxes())

pglet.app("textbox-control-samples", target = main)

input("Press Enter to exit...")