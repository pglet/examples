import pglet
from pglet import Button
with pglet.page("myapp") as page:
    page.clean()
    page.add(
      Button("Create account", icon='AddFriend', primary=True),
      Button("New item", icon='Add'),
      Button("Delete", icon='Delete'))