import sqlite3 #import sql libary from python already preinstalled

conn=sqlite3.connect("lite.db") #create connection to db(pass database file)
cur=conn.cursor() #create cursor within db
cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)") # create table named store containing 3 rows (item, quantity, price)
conn.commit() #commit changes
conn.close() #close connection
