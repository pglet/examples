import pglet
from pglet import Stack, Text

page = pglet.page()

stack = Stack(controls=[
       Text('Squares', size='large'),
        Stack(horizontal=True, controls=[
            Text('left top', align='left', vertical_align='top', width=100, height=100, bgcolor='salmon', color='white', padding=5),
            Text('center top', align='center', vertical_align='top', width=100, height=100, bgcolor='salmon', color='white', padding=5, size='large', border='1px solid #555'),
            Text('right top', align='right', vertical_align='top', width=100, height=100, bgcolor='salmon', color='white', padding=5, border='2px solid #555')
        ]),
        Stack(horizontal=True, controls=[
            Text('left center', align='left', vertical_align='center', width=100, height=100, bgcolor='PaleGoldenrod', padding=5),
            Text('center center', align='center', vertical_align='center', width=100, height=100, bgcolor='PaleGoldenrod', padding=5, size='large', border='1px solid #555'),
            Text('right center', align='right', vertical_align='center', width=100, height=100, bgcolor='PaleGoldenrod', padding=5, border='2px solid #555')
        ]),
        Stack(horizontal=True, controls=[
            Text('left bottom', align='left', vertical_align='center', width=100, height=100, bgcolor='PaleGreen', padding=5),
            Text('center bottom', align='center', vertical_align='center', width=100, height=100, bgcolor='PaleGreen', padding=5, size='large', border='1px solid #555'),
            Text('right bottom', align='right', vertical_align='center', width=100, height=100, bgcolor='PaleGreen', padding=5, border='2px solid #555')
        ]),
        Text('Circles', size='large'),
        Stack(horizontal=True, controls=[
            Text('regular', align='center', vertical_align='center', width=100, height=100, border_radius=50, bgcolor='salmon'),
            Text('bold italic', bold=True, italic=True, align='center', vertical_align='center', width=100, height=100, border_radius=50, bgcolor='PaleGoldenrod', size='large', border='1px solid #555'),
            Text('bold', bold=True, align='center', vertical_align='center', width=100, height=100, border_radius=50, bgcolor='PaleGreen', border='2px solid #555')

        ])
])

page.add(stack)
