import pglet
from pglet import Button
with pglet.page("buttons-with-icons") as page:
    page.add(
      Button("Create account", icon='AddFriend', primary=True),
      Button("New item", icon='Add'),
      Button("Delete", icon='Delete'))