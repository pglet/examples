import pglet
from pglet import Stack, Text, Button, Dialog, ChoiceGroup, Message
from pglet import choicegroup 

def dialogs(page):

  message = Message(dismiss=True, visible=False)

  def dialog_dismissed(e):
    message.value = f'Dialog "{e.data}" is dismissed'
    message.visible = True
    page.update()

  dialog1 = Dialog(title='Hello', on_dismiss=dialog_dismissed, data='dialog1', controls=[
    Text('Hi, are you OK?')], footer=[
        Button(text='Yes'),
        Button(text='No')
    ])
  
  dialog2 = Dialog(type='largeHeader', title='Missing Subject', on_dismiss=dialog_dismissed, data='dialog2', sub_text='Do you want to send this message without a subject?', controls=[
    ChoiceGroup(options=[
        choicegroup.Option('Option1'),
        choicegroup.Option('Option2'),
        choicegroup.Option('Option3'),
      ])
  ], footer = [
    Button(primary=True, text='Yes'),
    Button(text='No')
  ])

  dialog3 = Dialog(type='close', blocking=True, title='Missing Subject', on_dismiss=dialog_dismissed, data='dialog3', sub_text='Do you want to send this message without a subject?', footer = [
    Button(primary=True, text='Yes'),
    Button(text='No')
  ])
    
  def button_clicked(e):
    if e.data == 'dialog1':
        dialog1.open = True
    elif e.data == 'dialog2':
        dialog2.open = True
    elif e.data == 'dialog3':
        dialog3.open = True
    page.update()

  return Stack(gap=30, controls=[
      message,
      Stack(horizontal_align='start', controls=[
          Text("Default dialog", size="xLarge"),
          Text("To open, click on the 'Open dialog' button. To dismiss, click on the area outside the dialog"),
          Button("Open dialog", on_click=button_clicked, data='dialog1'),
          dialog1
      ]),
      Stack(horizontal_align='start', controls=[
          Text("Dialog with large header and ChoiceGroup", size="xLarge"),
          Text("To open, click on the 'Open dialog' button. To dismiss, click on the area outside the dialog"),
          Button("Open dialog", on_click=button_clicked, data='dialog2'),
          dialog2
      ]),
      Stack(horizontal_align='start', controls=[
          Text("Blocking Dialog", size="xLarge"),
          Text("A blocking Dialog disables all other actions and commands on the page behind it. To dismiss this dialog, click on the X button"),
          Button("Open dialog", on_click=button_clicked, data='dialog3'),
          dialog3
      ])
  ])

def main(page):
    
  page.title = "Dialog control samples"
  page.update()
  page.add(dialogs(page))

pglet.app("dialog-control-samples", target = main)

input("Press Enter to exit...")