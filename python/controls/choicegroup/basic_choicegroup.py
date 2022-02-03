import pglet
from pglet import ChoiceGroup
from pglet import choicegroup
with pglet.page("myapp") as page:
  page.clean()
  from pglet import Button, Text
  def button_clicked(e):
    t.value = f"ChoiceGroup value is:  {cg.value}"
    page.update()

  t = Text()
  b = Button(text='Submit', on_click=button_clicked)
  cg = ChoiceGroup(label='Select color', options=[
    choicegroup.Option('Red'),
    choicegroup.Option('Green'),
    choicegroup.Option('Blue')])
  
  page.add(cg, b, t)
  input()