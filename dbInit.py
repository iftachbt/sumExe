import sqlite3

connection = sqlite3.connect('iftachDB.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (userName,userPassword) VALUES (?, ?)",
            ('userAdmin', '123123')
            )
connection.commit()
connection.close()