import pglet
from pglet import Text, Progress, Stack

page = pglet.page()
page.horizontal_align = 'stretch'

stack = Stack(controls=[
            Text("Indeterminate Progress", size='xLarge'),
            Progress("Operation progress", description="Doing something indefinite...", width='50%')
        ])


page.add(stack)