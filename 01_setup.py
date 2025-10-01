# 01_setup.py
# Creates a SQLite database (mini_shop.db), builds tables, seeds sample data, and prints a quick sanity check.

import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

DB_PATH = Path("mini_shop.db")

def run():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # nicer dict-like row access
    cur = conn.cursor()

    # 1) Create tables (id as INTEGER PRIMARY KEY makes SQLite auto-increment)
    cur.executescript("""
    DROP TABLE IF EXISTS orders;
    DROP TABLE IF EXISTS products;
    DROP TABLE IF EXISTS customers;

    CREATE TABLE customers (
        id        INTEGER PRIMARY KEY,
        name      TEXT NOT NULL,
        email     TEXT UNIQUE,
        city      TEXT
    );

    CREATE TABLE products (
        id        INTEGER PRIMARY KEY,
        name      TEXT NOT NULL,
        price     REAL NOT NULL CHECK (price >= 0)
    );

    CREATE TABLE orders (
        id           INTEGER PRIMARY KEY,
        customer_id  INTEGER NOT NULL,
        product_id   INTEGER NOT NULL,
        quantity     INTEGER NOT NULL CHECK (quantity > 0),
        ordered_at   TEXT NOT NULL, -- ISO timestamp
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (product_id)  REFERENCES products(id)
    );
    """)

    # 2) Seed customers
    customers = [
        ("Aisha Khan",      "aisha@example.com",     "London"),
        ("Ben Williams",    "ben.w@example.com",     "Manchester"),
        ("Chitra Sundaram", "chitra@example.com",    "Birmingham"),
        ("Diego Lopez",     "diego.lopez@example.com","London"),
        ("Emma Davis",      "emma.d@example.com",    "Leeds"),
    ]
    cur.executemany("INSERT INTO customers (name, email, city) VALUES (?, ?, ?);", customers)

    # 3) Seed products
    products = [
        ("Notebook", 3.50),
        ("Pen", 1.20),
        ("Backpack", 24.99),
        ("Water Bottle", 9.99),
        ("Highlighter", 2.40),
    ]
    cur.executemany("INSERT INTO products (name, price) VALUES (?, ?);", products)

    # 4) Seed orders (spread across a few days)
    now = datetime.utcnow()
    orders = [
        (1, 1, 2, (now - timedelta(days=5)).isoformat(timespec="seconds")),
        (1, 3, 1, (now - timedelta(days=4)).isoformat(timespec="seconds")),
        (2, 2, 5, (now - timedelta(days=3)).isoformat(timespec="seconds")),
        (3, 4, 1, (now - timedelta(days=2)).isoformat(timespec="seconds")),
        (4, 1, 3, (now - timedelta(days=1)).isoformat(timespec="seconds")),
        (5, 5, 2, (now - timedelta(hours=12)).isoformat(timespec="seconds")),
    ]
    # orders: (customer_id, product_id, quantity, ordered_at)
    cur.executemany(
        "INSERT INTO orders (customer_id, product_id, quantity, ordered_at) VALUES (?, ?, ?, ?);",
        orders
    )

    conn.commit()

    # 5) Quick sanity checks: count rows and preview a few
    print("Database created at:", DB_PATH.resolve())
    print()

    def quick_preview(title, sql, params=()):
        print(f"--- {title} ---")
        cur.execute(sql, params)
        rows = cur.fetchall()
        for r in rows:
            print(dict(r))
        print()

    quick_preview("Customers (first 3)", "SELECT * FROM customers ORDER BY id LIMIT 3;")
    quick_preview("Products", "SELECT * FROM products ORDER BY id;")
    quick_preview("Orders (first 5)", "SELECT * FROM orders ORDER BY id LIMIT 5;")

    conn.close()

if __name__ == "__main__":
    run()
