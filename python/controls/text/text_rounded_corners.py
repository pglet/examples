import pglet
from pglet import Text, Stack
with pglet.page("text-rounded-corners") as page:
  
  page.add(Stack(horizontal=True, controls=[
    Text('Border radius 10% of width/height', align='center', vertical_align='center', width=100, height=100, border_radius=10, bgcolor='salmon'),
    Text('Border radius 25% of width/height', align='center', vertical_align='center', width=100, height=100, border_radius=25, bgcolor='PaleGoldenrod', border='1px solid #555'),
    Text('Border radius 50% of width/height', align='center', vertical_align='center', width=100, height=100, border_radius=50, bgcolor='PaleGreen', border='2px solid #555')
    ])
  )

  
