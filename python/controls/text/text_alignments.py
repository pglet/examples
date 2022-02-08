import pglet
from pglet import Text, Stack
with pglet.page("text-alignments") as page:
  
  page.add(
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
            Text('left bottom', align='left', vertical_align='bottom', width=100, height=100, bgcolor='PaleGreen', padding=5),
            Text('center bottom', align='center', vertical_align='bottom', width=100, height=100, bgcolor='PaleGreen', padding=5, size='large', border='1px solid #555'),
            Text('right bottom', align='right', vertical_align='bottom', width=100, height=100, bgcolor='PaleGreen', padding=5, border='2px solid #555')
        ]))
  
