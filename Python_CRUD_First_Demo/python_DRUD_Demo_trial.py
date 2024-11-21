import sqlite3

conn = sqlite3.connect("C:\\Users\\vijis\\Data_platform_development\\SQL Lite\\demo1.db")

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS people24(
            people_id INTEGER PRIMARY KEY, first_name TEXT UNIQUE, sur_name TEXT
            )''')


namesList = [
    (1, "Richard", "Chalk"),
    (2, "Sebastian", "Simon"),
    (3, "Stefan", "Holmberg"),
    (4, "Marcus", "Ottoson"),
    (5, "Tim", "Hydman"),
    (6, "Kristofer", "Fangrat"),
    (7, "Viji", "Soma"),
    (8, "Rajneet", "Kaur"),
    (10, "Rajneet", "Kaur"), 
    (12, "Rajneet", "Kaurr"),
    (12, "Rajneet", "Kaur")
]

cur.executemany('''
INSERT OR IGNORE INTO people24(people_id, first_name, sur_name)
                VALUES(?,?,?)''', namesList)

#Skriv ut samtliga namn i databasen till terminalen
cur.execute("SELECT * FROM people24")
record = cur.fetchall()
print(record)

conn.commit()

cur.close()
conn.close()