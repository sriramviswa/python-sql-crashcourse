# Example 3 (fixed): WHERE filters with a helper function

import sqlite3
from pathlib import Path

DB_PATH = Path("mini_shop.db")  # path to our SQLite DB file

# helper: run a query and print results with a label
def sql_query_and_print(cursor, query, comment=""):
    print("\n--- " + comment + " ---")   # label for readability
    cursor.execute(query)                 # run SQL
    for row in cursor.fetchall():         # fetch all results
        print(dict(row))                  # print as a dict

def run():
    # connect and prepare cursor (rows as dict-like objects)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # 1) customers from London (matches customers.city)
    sql_query_and_print(cur,
                        "SELECT * FROM customers WHERE city = 'London';",
                        "Customers from London")

    # 2) products priced > 5 (matches products.price)
    sql_query_and_print(cur,
                        "SELECT * FROM products WHERE price > 5;",
                        "Products costing more than 5")

    # 3) orders placed by customer #1 (matches orders.customer_id)
    sql_query_and_print(cur,
                        "SELECT * FROM orders WHERE customer_id = 1;",
                        "Orders from Customer ID = 1")

    conn.close()  # tidy up

if __name__ == "__main__":
    run()
