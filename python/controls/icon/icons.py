import pglet
from pglet import Icon, Stack
with pglet.page("icons") as page:
  page.add(
    Stack(horizontal=True, controls=[
      Icon("ChangeEntitlements", color='Magenta20'),
      Icon("shop", color='CyanBlue10'),
      Icon("TrainSolid")
    ]),
    Stack(horizontal=True, vertical_align='center', controls=[
      Icon("BlockedSite", color='Orange20', size=25),
      Icon("settings", color='Gray20', size=50),
      Icon("save", color='Blue10', size=100)
    ])        
  )