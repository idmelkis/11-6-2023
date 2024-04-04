import sqlite3

db = sqlite3.connect("database.db")
cur = db.cursor()

# class Lietotajs:
#     def __init__(self, id, lietotajvards, parole, epasts) -> None:
#         self.id = id
#         self.lietotajvards = lietotajvards
#         self.parole = parole
#         self.epasts = epasts
# https://www.sqlite.org/lang_createtable.html
# https://stackoverflow.com/questions/4098008/create-table-in-sqlite-only-if-it-doesnt-exist-already
# True = 1
# False = 0
create_db = "CREATE TABLE IF NOT EXISTS Lietotajs (\
    id INTEGER UNIQUE NOT NULL,\
    Lietotajvards TEXT NOT NULL,\
    Parole TEXT,\
    Epasts TEXT,\
    PRIMARY KEY(id AUTOINCREMENT)\
)"
cur.execute(create_db)

# Uzdevums: Izveidojat otro tabulu ar kolonām:
# ID (integer), Nosaukums (text), Cena (real), Apraksts (text)
create_db = "CREATE TABLE IF NOT EXISTS Prece (\
    id INTEGER UNIQUE NOT NULL,\
    Nosaukums TEXT,\
    Cena REAL,\
    Apraksts TEXT,\
    PRIMARY KEY(id AUTOINCREMENT)\
)"
cur.execute(create_db)

# INSERT INTO
# https://www.sqlite.org/lang_insert.html
# insert_data = 'INSERT INTO Lietotajs (Lietotajvards, Parole)\
#     VALUES ("skolens", "hunter2")'
#l1 = Lietotajs(1, "skolens", "hunter2", None)
# cur.execute(insert_data)

# Uzdevums: Ievietot tabulā "Prece" sekojošus datus:
# Nosaukums: "Lineāls"
# Cena: 0.50
# Apraksts: "Parasts plastmasas lineāls"
# insert_data = 'INSERT INTO Prece (Nosaukums, Cena, Apraksts)\
#     VALUES ("Lineāls", 0.5, "Parasts plastmasas lineāls")'
# cur.execute(insert_data)

class Lietotajs:
    def __init__(self, id, lietotajvards, parole, epasts) -> None:
        self.id = id
        self.lietotajvards = lietotajvards
        self.parole = parole
        self.epasts = epasts
    def __str__(self) -> str:
        return f"Lietotājs {self.id} ar lietotājvārdu {self.lietotajvards}"
class Prece:
    def __init__(self, id, nosaukums, cena, apraksts) -> None:
        self.id = id
        self.nosaukums = nosaukums
        self.cena = cena
        self.apraksts = apraksts
    def __str__(self) -> str:
        return f"Prece {self.nosaukums}"
#l1 = Lietotajs(1, "skolens", "hunter2", None)
#lin = Prece(1, "Lineāls", 0.5, "Parasts plastmasas lineāls")
        
#select_query = "SELECT id, lietotajvards, parole, epasts FROM lietotajs WHERE ..."
select_query = "SELECT * FROM lietotajs WHERE id = 3"
cur.execute(select_query)
rows = cur.fetchmany()
for row in rows:
    l1 = Lietotajs(row[0], row[1], row[2], row[3])
    print(l1)

# Uzdevums: Iegūt no tabulas Prece visus datus kolonās 
# "Nosaukums" un "Apraksts"
select_query = "SELECT Nosaukums, Apraksts FROM Prece"
cur.execute(select_query)
rows = cur.fetchmany()
for row in rows:
    l1 = Prece(0, row[0], 0, row[1])
    print(l1)

cur.close()
db.commit()
db.close()