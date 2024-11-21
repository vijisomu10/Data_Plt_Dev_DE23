import sqlite3

conn = sqlite3.connect("C:\\Users\\vijis\\Data_platform_development\\SQL Lite\\demo1.db")

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS people100(
            first_name TEXT, sur_name TEXT UNIQUE
            )''')


namesList = [
    ("Richard", "Chalk"),
    ("Sebastian", "Simon"),
    ("Stefan", "Holmberg"),
    ("Marcuss", "Ottoson"),   
    ("Tim", "Hydman"),
    ("Kristofer", "Fangrat"),
    ("Marcus", "Ottoson"),
    ("Viji", "Soma"),
    ("Rajneet", "Kaur"),
    ("Rajneet", "Kaur"),
    ("Viji", "Somas")
]

cur.executemany('''
INSERT OR IGNORE INTO people100(first_name, sur_name)
                VALUES(?,?)''', namesList)

#Skriv ut samtliga namn i databasen till terminalen
cur.execute("SELECT * FROM people100")
record = cur.fetchall()
print(record)

conn.commit()

cur.close()
conn.close()