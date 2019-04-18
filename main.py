#Initialize scanners

#Initialize database

from flask import Flask, render_template
from openpyxl import load_workbook
from xlsx2html import xlsx2html

import sqlite3


inventory_db = 'databases/inventory.db'
dest = 'inventory.xlsx'
wb = load_workbook(filename = dest)
mysheet = wb['Sheet1']
vodka = mysheet['D6'].value


def change_val(cell, target_value):
	mysheet[str(cell)] = target_value 
	wb.save(filename = dest)


from helpers.sql import conn_db	






app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('bootstraptemplate/index.html')

if __name__ == '__main__':
   app.run(debug = True)



"""
Host a webserver on the pi
Have live refresh on the browser being used.
Login with your creds to webserver. Pulls up main inventory page which is authenticated.


"""

#Show the inventory table online in a neat grid format. Use emojis for icons.

#Make a database for data.

#Tables:

#    users
#    transactions
#    vendors
#    invoices

#Scan in invoices to be examined later online easily with pdf viewer.

#Show verbose log of every order that goes through.

#Every time a transaction is ran through, the item is sent to the terminal.

#Save logs of all our transactions so you dont have to print a merchant copy.

#Make an FTP server to host the files.

