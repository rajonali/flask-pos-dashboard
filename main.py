#Initialize scanners

#Initialize database

from flask import Flask, render_template
from openpyxl import load_workbook
from xlsx2html import xlsx2html




from flask import Flask, request, send_from_directory

import os



inventory_db = 'databases/transactions.db'

import sqlite3

conn = sqlite3.connect(inventory_db)
cur = conn.cursor()



con = sqlite3.connect("databases/transactions.db")
con.row_factory = sqlite3.Row   
cur = con.cursor()


#Parse json products and put into log file
cur.execute("SELECT * FROM receipts")
rows = cur.fetchall()
for row in rows:
    print(row)


app = Flask(__name__, static_url_path='/static')










@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)



@app.route("/register.html", methods=["GET"])
def register():
    return render_template('/register.html')

@app.route("/login.html", methods=["GET"])
def login():
    return render_template('/login.html')

@app.route("/forgot-password.html", methods=["GET"])
def forgot_password():
    return render_template('/forgot-password.html')


@app.route("/404.html", methods=["GET"])
def fourohfour():
    return render_template('/404.html')



@app.route("/salesreport.html", methods=["GET"])
def salesreport():
    return render_template('/salesreport.html')




 

@app.route('/')
def hello_world():
	return render_template('index.html', items = rows)

if __name__ == '__main__':
   app.run(debug = True)

#app.run(host='0.0.0.0',port=8080)


