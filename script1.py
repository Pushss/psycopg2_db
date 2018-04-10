import sqlite3 #import sql libary from python already preinstalled

def create_table(): #function to create table if not already created
    conn=sqlite3.connect("lite.db") #create connection to db(pass database file)
    cur=conn.cursor() #create cursor within db
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") # create table named store containing 3 rows (item, quantity, price)
    conn.commit() #commit changes
    conn.close() #close connection

def insert(item,quantity,price): #function to insert data using insert("coffer cup",3,1.5)
        conn=sqlite3.connect("lite.db") #create connection to db(pass database file)
        cur=conn.cursor() #create cursor within db
        cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price)) #Insert data into values (inserted in order)
        conn.commit() #commit changes
        conn.close() #close connection

insert("coffer cup",3,1.5)

def view(): #function to view the db in console
    conn=sqlite3.connect("lite.db") #create connection to db(pass database file)
    cur=conn.cursor() #create cursor within db
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall() #variable storing all data from TABLE store
    conn.close() #close conection to db
    return rows #return variable storing all data from the TABLE

print(view()) #print db rows as list
