import pglet
from pglet import Stack, Text, ChoiceGroup
from pglet import choicegroup

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("ChoiceGroup with icons", size="xLarge"),
    ChoiceGroup(label='Pick one icon', options=[
      choicegroup.Option(key='day', text='Day', icon='CalendarDay'),
      choicegroup.Option(key='week', text='Week', icon='CalendarWeek'),
      choicegroup.Option(key='month', text='Month', icon='Calendar')
  ])
  ])

page.add(stack)