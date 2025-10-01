# Python + SQL Crash Course 🐍🗄️

This is my personal crash course in SQL using Python (SQLite).  
I put together 25 small examples to practice the basics — from creating a database and writing simple SELECTs to more advanced queries.

---

## What's inside
- Example 1: Create a database and add sample data  
- Example 2: Basic `SELECT` queries  
- Example 3: Filtering with `WHERE`  
- Example 4: Sorting with `ORDER BY`  
- Example 5: Limiting results with `LIMIT` & `OFFSET`  
- ... up to Example 25 (joins, subqueries, views, etc.)

Each example is a short Python script with comments that explain the SQL.

---

## How to run
Clone the repo and run with Python 3.8+:

```bash
git clone https://github.com/<YOUR_USERNAME>/python-sql-crashcourse.git
cd python-sql-crashcourse
python 01_setup.py
python 02_select.py
# ... etc.
```

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
```bash
# Example: SELECT with WHERE filter
  cur.execute("SELECT * FROM products WHERE price > 5;")
  for row in cur.fetchall():
    print(dict(row))
```
Output:
```bash
  {'id': 3, 'name': 'Backpack', 'price': 24.99}
  {'id': 4, 'name': 'Water Bottle', 'price': 9.99}
```
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


---
## 📝 Learning Note
This project was built as part of my self-study journey.  
I practiced SQL queries using Python with guidance from OpenAI’s ChatGPT, while writing and refining the code myself.  

The goal was not just to generate answers but to deeply understand and practice SQL step by step.

