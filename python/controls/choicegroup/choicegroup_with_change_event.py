import pglet
from pglet import ChoiceGroup, choicegroup, Text
with pglet.page("choicegroup-with-change-event") as page:
  
  def choicegroup_changed(e):
        t.value = f"ChoiceGroup value changed to {cg.value}" 
        t.update()

  cg = ChoiceGroup(label='Select color', on_change=choicegroup_changed, options=[
    choicegroup.Option('Red'),
    choicegroup.Option('Green'),
    choicegroup.Option('Blue')
  ])

  t = Text()

  page.add(cg, t)

  input()