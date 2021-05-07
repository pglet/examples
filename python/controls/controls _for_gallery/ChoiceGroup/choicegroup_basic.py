import pglet
from pglet import Stack, Text, ChoiceGroup
from pglet import choicegroup

page = pglet.page()

stack = Stack(gap=20, controls=[
    Text("Basic ChoiceGroup", size="xLarge"),
    ChoiceGroup(label='Select color', options=[
        choicegroup.Option('Red'),
        choicegroup.Option('Green'),
        choicegroup.Option('Blue')
  ])
  ])

page.add(stack)