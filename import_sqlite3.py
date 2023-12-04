import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE accounts (username TEXT, password TEXT)')
conn.close()