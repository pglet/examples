import pglet
from pglet import Stack, Text, Toggle

page = pglet.page()

def toggle_with_on_change(page):
    
    def toggle_changed(e):
      if t.value:
        # Dark theme
        page.theme_background_color = '#262626'
        page.theme_primary_color = '#3ee66d'
        page.theme_text_color = '#edd2b7'
      else:
        page.theme_background_color = ''
        page.theme_primary_color = ''
        page.theme_text_color = ''
      
      page.update()

    t = Toggle(label="Click to change the page theme", on_text="Dark theme", off_text="Light theme", value=False, on_change=toggle_changed)
    return t

stack = Stack(gap=20, controls=[
    Text("Toggle with Change event", size="xLarge"),
    toggle_with_on_change(page)
])

page.add(stack)

input("Press Enter to exit...")