import sqlite3
from pathlib import Path

DB_PATH = Path("mini_shop.db")

def show_schema(cur, table):
    cur.execute(f"PRAGMA table_info({table});")
    print(f"\n--- schema; {table} ---")
    for cid, name, coltype, notnull, dflt, pk in cur.fetchall():
        print({"col_index": cid, "name" : name, "type" : coltype, "pk" : pk, "notnull" : notnull, "default" : dflt})
    
def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    show_schema(cur, "customers")
    show_schema(cur, "products")
    show_schema(cur, "orders")

    conn.close()


if __name__ == "__main__":
    run()