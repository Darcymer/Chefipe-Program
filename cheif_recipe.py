import sqlite3

conn = sqlite3.connect("recipies.db")
curs = conn.cursor