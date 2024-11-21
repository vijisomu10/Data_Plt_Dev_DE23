import sqlite3

conn = sqlite3.connect("C:\\Users\\vijis\\Data_platform_development\\SQL Lite\\script1.db")

cur = conn.cursor()

file_path = "C:\\Users\\vijis\\Data_platform_development\\Python_CRUD_Script_Demo\\script.sql"
with open(file_path) as file:
    sqlScript = file.read()

cur.executescript(sqlScript)

memberData = cur.execute("SELECT id, fn FROM members WHERE fn = 'Homer' ")
for m in memberData:
    print(m)

cur.close()
conn.close()