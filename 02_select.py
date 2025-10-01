# Example 2: Basic SELECT queries using SQLite + Python

# --- Import libraries ---
import sqlite3                # library to work with SQLite databases
from pathlib import Path      # helps us handle file paths safely

# --- Path to our database file ---
DB_PATH = Path("mini_shop.db")   # mini_shop.db was created in Example 1

def run():
    # --- Step 1: Connect to the database ---
    conn = sqlite3.connect(DB_PATH)        # create connection object
    conn.row_factory = sqlite3.Row         # rows behave like dicts (easy to read by column name)
    cur = conn.cursor()                    # cursor is used to run SQL commands

    # --- Step 2: Run queries and fetch results ---

    # Query 1: Select * (all columns from customers)
    print("\n--- All Customers (SELECT *) ---")
    cur.execute("SELECT * FROM customers;")   # run SQL
    for row in cur.fetchall():                # fetch all rows returned
        print(dict(row))                      # convert each row to a dict for easy printing

    # Query 2: Select only name + city from customers
    print("\n--- Just names and cities ---")
    cur.execute("SELECT name, city FROM customers;")  # only 2 columns
    for row in cur.fetchall():
        print(dict(row))

    # Query 3: Select * from products
    print("\n--- All Products ---")
    cur.execute("SELECT * FROM products;")
    for row in cur.fetchall():
        print(dict(row))

    # --- Step 3: Close connection when done ---
    conn.close()

# --- Program entry point ---
if __name__ == "__main__":
    run()
