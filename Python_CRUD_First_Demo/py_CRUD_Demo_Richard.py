# Step 1a
# Denna rad importerar SQLite3-modulen till ditt Python-program. 
# SQLite3 är ett bibliotek som tillåter Python att interagera med SQLite-databaser. 
# SQLite är en inbyggd, lättviktig databashanterare.
import sqlite3

# Step 1b
# Här skapas en anslutning till en SQLite-databas. Om databasfilen ("demo1.db") inte finns på den angivna 
# sökvägen (C:\\Db\\SQL Lite\\), kommer SQLite att skapa den automatiskt. 
# conn är en variabel som representerar denna anslutning.
conn = sqlite3.connect(
   "C:\\Users\\vijis\\Data_platform_development\\SQL Lite\\demo_richard.db")

# Step 1c
# Denna rad skapar ett 'cursor' objekt med hjälp av anslutningsobjektet conn. 
# En 'cursor' är som en markör eller pekare som du använder 
# för att utföra operationer (som att köra SQL-kommandon) på databasen.
cur = conn.cursor()

# Step 1d - Option 1
# Skapa en tabel som heter "people". Denna skapa error om tabellen people redan finns :(
# OBS: Det är också möjligt att anropa conn.execute()
# cur.execute('''CREATE TABLE people(firstName TEXT, surName TEXT)''')


# Step 1d - Option 2 (better!)
# Skapa en tabel som heter "people" om den inte redan existerar!
# OBS: Det är också möjligt att anropa conn.execute()
cur.execute('''CREATE TABLE IF NOT EXISTS people_new
            (firstName TEXT, surName TEXT)''')

# Step 2a
namesList = [
  ("Richard", "Chalk"),
  ("Sebastian", "S"),
  ("Stefan", "H"),
  ("Marcus", "B")
]

# Step 2b - Option 1, Denna variant är OK...
# Men den kommer att fortsätta lägga till samma personer om och om igen!
# cur.executemany('''INSERT INTO people (firstName, surName) VALUES (?,?)''', namesList)

# Låt eleverna köra programmet här... Man ser att personer blir dubbletter!
# radera databasen... kör om scriptet... nu skapas inte dubletter :)

# Step 2b - Option 2 (better)
# Nu läggs endast dessa personer till om de inte redan fanns i databsen!
for name in namesList:
    # Kontrollera om personen redan finns i databasen
    cur.execute("SELECT * FROM people_new WHERE firstName = ? AND surName = ?", name)
    result = cur.fetchone()
    
    # Om personen inte finns, lägg till den
    if result is None:
        cur.execute("INSERT INTO people_new (firstName, surName) VALUES (?, ?)", name)
        conn.commit()


# Step 2c
# Nu kan vi skriva ut samtliga namn från people tabellen i vår db!
peopleData = cur.execute("SELECT * FROM people_new")
for n in peopleData:
  print(n)

# Step 1e
# Det är ett metodanrop som bekräftar alla ändringar som gjorts i databasen sedan den senaste commit. 
# I det här fallet bekräftar den skapandet av den nya tabellen. 
conn.commit()

# Step 1f
# Till slut stänger vi vår cursor
cur.close()

# Step 1g
# Stäng connection till vår databas. Det är viktigt att stänga anslutningen 
# när du är klar med den för att frigöra systemresurser.
conn.close()