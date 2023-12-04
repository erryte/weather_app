import sqlite3

# add line to have change in order to initiate a PR
conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE accounts (username TEXT, password TEXT)')
conn.close()
