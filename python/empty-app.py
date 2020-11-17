import pglet

def main(p):
    p.send("set page title=aaa")
    r1 = p.send("add row")
    c1 = p.send(f"add col to={r1}")
    p.send(f"add text value='This is app session {p.conn_id}' to={c1}")

pglet.app("app1", target=main)