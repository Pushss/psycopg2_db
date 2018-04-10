import psycopg2 #import psycopg2 libary

def create_table(): #function to create table if not already created
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'") #create connection to db(pass database file)
    cur=conn.cursor() #create cursor within db
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") # create table named store containing 3 rows (item, quantity, price)
    conn.commit() #commit changes
    conn.close() #close connection

def insert(item,quantity,price): #function to insert data using insert("coffer cup",3,1.5)
        conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'") #create connection to db(pass database file)
        cur=conn.cursor() #create cursor within db
        cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price)) #Insert data into values (inserted in order)
        conn.commit() #commit changes
        conn.close() #close connection

def view(): #function to view the db in console
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'") #create connection to db(pass database file)
    cur=conn.cursor() #create cursor within db
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall() #variable storing all data from TABLE store
    conn.close() #close conection to db
    return rows #return variable storing all data from the TABLE

def delete(item): #delete date cotaining specified item
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'") #create connection to db(pass database file)
    cur=conn.cursor() #create cursor within db
    cur.execute("DELETE FROM store WHERE item=%s",(item,)) #Delete row containing the item e.g. delete("coffee cup")
    conn.commit() #commit changes to db
    conn.close() #close conection to db

def update(quantity,price,item): #function to update row within TABLE
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'") #create connection to db(pass database file)
    cur=conn.cursor() #create cursor within db
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item =%s",(quantity,price,item)) #Will update data in database where row contains the specified ITEM
    conn.commit() #commit changes to db
    conn.close() #close conection to db

create_table()
#insert("Orange",10,15.5) #insert data into db
#delete("coffee cup") #delete any rows containing coffee cup
update(11,6,"Orange") #update rows containing Orange with new values
print(view()) #print db rows as list
