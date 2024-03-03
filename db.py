import sqlite3

def getDBConnnection():
  con = sqlite3.connect('iftachDB.db')
  con.row_factory = sqlite3.Row
  return con

def createUser(userName,password):
  print("got to createUser",userName,password)
  con = getDBConnnection()
  con.execute('INSERT INTO users (userName,userPassword) VALUES (?, ?)',(userName,password))
  con.commit()
  con.close()
  return 'index'

def fetchUser(userName):
  con = getDBConnnection()
  user = con.execute('SELECT * WHERE userName = ? FROM posts',(userName))
  con.close()
  return user
