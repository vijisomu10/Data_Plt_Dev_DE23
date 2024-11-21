import sqlite3

#connect a database
conn = sqlite3.connect(
    '\\Users\\vijis\\Data_platform_development\\SQL Lite\\customer.db')

#create a cursor
cur = conn.cursor()

#Create a Table
# cur.execute(''' 
#     CREATE TABLE IF NOT EXISTS customers(
#             first_name TEXT,
#             last_name TEXT,
#             email TEXT
#     )''')

#insert one record in the table customers
# cur.execute("INSERT INTO customers VALUES('John', 'Doe', 'john@gmail.com')")

#insert more than one record in table customers
# customerList = [
#     ('John', 'Paul', 'paul@gmail.com'),
#     ('Soma', 'Sanjiv', 'soma.san@outlook.com')
# ]
# cur.executemany("INSERT INTO customers VALUES(?,?,?)", customerList)

#find row ID in the database 
#cur.execute('SELECT rowid, * FROM customers')

cur.execute('SELECT rowid, * FROM customers')
items = cur.fetchall()

for item in items:
    print(item)

print('Command executed successfully')

#commit our command
conn.commit()

#close our connection
conn.close()