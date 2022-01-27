import pglet
from pglet import ChoiceGroup
from pglet import choicegroup
with pglet.page("myapp") as page:
  page.clean()
  from pglet import Text
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