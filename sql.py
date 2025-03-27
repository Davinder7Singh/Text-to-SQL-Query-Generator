import sqlite3
import random

# Connect to SQLite database
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

# Create EMPLOYEE table
cursor.execute('''
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT,
    DEPARTMENT TEXT,
    SALARY INTEGER
);
''')

# Sample data for names and departments
names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Sarah", "David", "Laura"]
departments = ["HR", "Finance", "IT", "Marketing", "Sales"]

# Insert 100 random employee records
for _ in range(100):
    name = random.choice(names)
    department = random.choice(departments)
    salary = random.randint(30000, 100000)
    cursor.execute("INSERT INTO EMPLOYEE (NAME, DEPARTMENT, SALARY) VALUES (?, ?, ?)", (name, department, salary))

# Commit changes and close connection
conn.commit()

# Display all records
print("All Employee Records:")
data = cursor.execute("SELECT * FROM EMPLOYEE")
for row in data:
    print(row)

conn.close()
