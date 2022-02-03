import pglet
from pglet import ChoiceGroup, choicegroup
with pglet.page("choicegroup-with-icons") as page:
  page.add(ChoiceGroup(label='Pick one icon', options=[
    choicegroup.Option(key='day', text='Day', icon='CalendarDay'),
    choicegroup.Option(key='week', text='Week', icon='CalendarWeek'),
    choicegroup.Option(key='month', text='Month', icon='Calendar')
  ]))