import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print('Tables in database:', [t[0] for t in tables])
conn.close()
