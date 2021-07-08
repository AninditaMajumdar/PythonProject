import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
query = "CREATE TABLE IF NOT EXISTS EMPLOYEE(emp_id  INTEGER PRIMARY KEY AUTOINCREMENT,emp_name text, project_name text,doj text)"
cursor.execute(query)
connection.commit()
connection.close()
