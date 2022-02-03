import pglet
from pglet import Button, Stack
with pglet.page("toolbar-buttons") as page:
    page.add(Stack(horizontal=True, controls=[
      Button(text="New item", toolbar=True, icon='Add'),
      Button(text="Send", toolbar=True, icon='Mail'),
      Button(text="Show example", toolbar=True, icon='ChevronDown'),
      Button(text="Delete", toolbar=True, icon_color='red', icon='Delete')
    ]))