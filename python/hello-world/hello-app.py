import pglet
from pglet import Text


def main(page):
    page.title = "Hello!"
    page.add(Text(f"Hello to session {page.session_id}!"))


pglet.app(target=main, web=False)
