import pglet
from pglet import Stack, Text

page = pglet.page()

stack = Stack(controls=[
        Text('Basic text controls', size='large'),
        Stack(horizontal=True, controls=[
            Text('default'),
            Text('bold', bold=True),
            Text('italic', italic=True),
            Text('preformatted', pre=True)
        ]),
        Stack(horizontal=True, controls=[
            Text('tiny', size='tiny'),
            Text('small', size='small'),
            Text('medium', size='medium'),
            Text('large', size='large'),
            Text('xLarge', size='xLarge') 
        ])
    ])

page.add(stack)