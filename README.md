🌟 MITALI EXPRESS POS (ME-POS) v.0.1



ME-POS REST API and Database Schema:


TODO:
Make a PO template and and invoice template



REST API ENDPOINTS:

/login
/register
/forgot


/product/viewproduct/####
/product/modifyproduct/###
/product/addproduct/###

/transaction/view/ + ###
/transaction/add/###
/transaction/modify/###


/auth/admin/adduser
/auth/admin/modifyuser

/auth/invoice/view
/auth/invoice/add



/auth/employee/###/clockin
/auth/employee/###/clockout




**Log all actions into a text logfile and parse into db later. Stream log-file to log window with auto refresh or use AJAX calls (TODO).


Cached data for every session at init:
	logs
	inventory/stock


DATABASE SCHEMA:

DBs < Tables < Columns
Blob = json object

NOTES:
**Try to minimize database modifications. If you need to void an order just flag it with a boolean


Every receipt of transactions stored here
transactions.db
	L receipts.table
		L receipt_id(auto inc int), date(string), time(string) , products(blob), voided(boolean)

Table of every item goes here
inventory.db
	L stock.db
		L product_name(text), product_id(auto inc int), product_upc(text), price(numerical), qty(numerical) , vendor(text), 


Scanned documents go here in blobs (archived)
financials.db
	L invoices.table
	L purchase_orders.table


Hashed user accounts
users.db
	L uid(text), pass(text), permission_level(int)

Logfiles stored in blobs go here.
log.db




TODO:

Host a webserver on the pi
Have live refresh on the browser being used.
Login with your creds to webserver. Pulls up main inventory page which is authenticated.


Show the inventory table online in a neat grid format. Use emojis for icons.

Make a database for data.

Tables:

    users
    transactions
    vendors
    invoices

Scan in invoices to be examined later online easily with pdf viewer.

Show verbose log of every order that goes through.

Every time a transaction is ran through, the item is sent to the terminal.

Save logs of all our transactions so you dont have to print a merchant copy.

Make an FTP server to host the files.




