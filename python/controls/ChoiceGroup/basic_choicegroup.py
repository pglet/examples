import pglet
from pglet import ChoiceGroup
from pglet import choicegroup
with pglet.page("myapp") as page:
  page.clean()
  page.add(ChoiceGroup(label='Select color', options=[
    choicegroup.Option('Red'),
    choicegroup.Option('Green'),
    choicegroup.Option('Blue')]))