import pglet
from pglet import Text
with pglet.page("text-size") as page:
  
  page.add(
    Text('tiny', size='tiny'),
    Text('xSmall', size='xSmall'),
    Text('small', size='small'),
    Text('smallPlus', size='smallPlus'),
    Text('medium', size='medium'),
    Text('mediumPlus', size='mediumPlus'),
    Text('large', size='large'),
    Text('xLarge', size='xLarge'),
    Text('xxLarge', size='xxLarge'),
    Text('superLarge', size='superLarge'),
    Text('mega', size='mega'))
  
  
