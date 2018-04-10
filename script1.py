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

insert("coffee cup",3,1.5) #insert data into db

def view(): #function to view the db in console
    conn=sqlite3.connect("lite.db") #create connection to db(pass database file)
    cur=conn.cursor() #create cursor within db
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall() #variable storing all data from TABLE store
    conn.close() #close conection to db
    return rows #return variable storing all data from the TABLE

print(view()) #print db rows as list

def delete(item): #delete date cotaining specified item
    conn=sqlite3.connect("lite.db") #create connection to db(pass database file)
    cur=conn.cursor() #create cursor within db
    cur.execute("DELETE FROM store WHERE item=?",(item,)) #Delete row containing the item e.g. delete("coffee cup")
    conn.commit() #commit changes to db
    conn.close() #close conection to db

def update(quantity,price,item): #function to update row within TABLE
    conn=sqlite3.connect("lite.db") #create connection to db(pass database file)
    cur=conn.cursor() #create cursor within db
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item =?",(quantity,price,item)) #Will update data in database where row contains the specified ITEM
    conn.commit() #commit changes to db
    conn.close() #close conection to db

update(11,6,"Water glass") #update rows containing Water glass with new values
print(view()) #print db rows as list
