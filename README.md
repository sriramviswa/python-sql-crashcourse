# Python + SQL Crash Course 🐍🗄️

Hands-on crash course to learn **SQL using Python (with SQLite)**.  
This repo contains 25 step-by-step examples that cover everything from creating a database to advanced queries.

---

## 📚 What’s inside
- Example 1: Create a database, tables, and seed sample data  
- Example 2: Basic `SELECT` queries  
- Example 3: Filtering with `WHERE`  
- Example 4: Sorting results with `ORDER BY`  
- Example 5: Limiting results with `LIMIT` & `OFFSET`  
- ... up to Example 25: Advanced patterns with parameterized queries & simple DAO  

Each example is written in Python with clear comments to explain the SQL concepts.

---

## 🚀 How to run
1. Clone the repo:

   git clone https://github.com/<YOUR_USERNAME>/python-sql-crashcourse.git
   cd python-sql-crashcourse

2. Run Python scripts (requires Python 3.8+):

  python 01_setup.py
  python 02_select.py
  python 03_where.py
  # ... etc.


Tip: Run 01_setup.py first — it creates the mini_shop.db SQLite database with sample data.
All other examples build on this database.
------------

🛠️ Tech stack

Python 3 (standard library only — no external dependencies)
SQLite (lightweight database engine built into Python)
-------------

🎯 Why this repo

I built this as a practical learning project:
To strengthen SQL basics using Python.
To create a reference I (and others) can revisit later.
To showcase hands-on coding practice in interviews.
-----------

✨ Example snapshot

# Example: SELECT with WHERE filter
  cur.execute("SELECT * FROM products WHERE price > 5;")
  for row in cur.fetchall():
    print(dict(row))

Output:

  {'id': 3, 'name': 'Backpack', 'price': 24.99}
  {'id': 4, 'name': 'Water Bottle', 'price': 9.99}
------------

📌 Next steps

Add more advanced queries (joins, subqueries, views, transactions, etc.)
Extend to PostgreSQL or MySQL to practice client/server DB concepts
Build small apps/dashboards on top of the data
------------


🤝 Contributions

This repo is mainly for personal learning, but feel free to fork, clone, and try the examples yourself.
PRs and suggestions are welcome if you have neat improvements!
------------

🧑‍💻 Author

Sriram Viswanathan
Product Manager | Creative Technology Enthusiast | SQL Learner
https://www.linkedin.com/in/sriram-vis
