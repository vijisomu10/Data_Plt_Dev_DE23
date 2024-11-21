import sqlite3
conn = sqlite3.connect('C:\\Users\\vijis\\Data_platform_development\\SQL Lite\\employeeRelation.db')
cur = conn.cursor()

file_path = 'C:\\Users\\vijis\\Data_platform_development\\Python_Relation_Demo\\script.sql'
with open(file_path) as file:
    sqlScript = file.read()

cur.executescript(sqlScript)


# SQL-fråga som använder LEFT JOIN för att sammanföra members och employer
query = """
        SELECT 
            m.fn AS Familjemedlem,
            m.ln AS Efternamn,
            e.employer_name AS Arbetsgivare
        FROM 
            members m
        LEFT JOIN 
            employer e ON m.employerFK = e.employer_id;
        """

# Exekvera frågan
cur.execute(query)

# Skriv ut resultaten
for row in cur.fetchall():
    print(row)


conn.commit()
cur.close()
conn.close()



