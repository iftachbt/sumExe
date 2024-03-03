import sqlite3
from flask import Flask,url_for, render_template, request, flash, redirect 
from db import createUser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wuba laba dub dub'

@app.route('/',methods=('GET','POST'))
def index():
  if request.method == 'POST':
      print("POST request received")
      username = request.form['username']
      password = request.form['password']
      createUser(username,password)
  elif request.method == 'GET':
      print("GET request received")
  return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')


