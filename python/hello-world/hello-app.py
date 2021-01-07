import pglet
from pglet import Text

class HelloWorldApp:
    def __init__(self, p):
        self.p = p
        self.main()
    
    def main(self):
        self.p.add(Text(value=f"Hello to session {self.p.conn_id}!"))

pglet.app(target=HelloWorldApp, web=True)