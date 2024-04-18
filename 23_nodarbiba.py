import sqlite3
db = sqlite3.connect('23_nodarbiba.db')
cur = db.cursor()
cur.execute("PRAGMA foreign_keys = ON;")

#cur.execute("DROP TABLE atzime")
# cur.execute("CREATE TABLE IF NOT EXISTS atzime (\
#             id INTEGER UNIQUE,\
#             prieksmets STRING,\
#             skolens STRING,\
#             atzime INTEGER,\
#             PRIMARY KEY (id AUTOINCREMENT)\
# )")

# Vairāku vērtību ievietošana
# cur.execute('INSERT INTO atzime (prieksmets, skolens, atzime) VALUES\
#             ("Matemātika", "Jānis", 6), ("Lat. valoda", "Pēteris", 9),\
#             ("Matemātika", "Māris", 2), ("Vācu Valoda", "Jana", 6),\
#             ("Krievu Valoda", "Anna", 9)')

# Sagrupējam pēc priekšmeta = izvadam katra priekšmeta lielāko atzīmi, un kam tā ir
# cur.execute('SELECT skolens, prieksmets, max(atzime) FROM atzime GROUP BY prieksmets')
# print(cur.fetchall())

# Tabulas izveide
cur.execute("DROP TABLE produkts")
cur.execute("CREATE TABLE IF NOT EXISTS produkts (\
            id INTEGER UNIQUE,\
            nosaukums STRING,\
            piegadatajs INTEGER,\
            cena FLOAT,\
            PRIMARY KEY (id AUTOINCREMENT)\
            FOREIGN KEY(piegadatajs) REFERENCES produkts(id) ON DELETE CASCADE\
)")

# Datu ievietošana
cur.execute("INSERT INTO produkts (nosaukums, cena) VALUES\
            (\"Telefons\", 1000.0),\
            (\"Dators\", 2000.0),\
            (\"Soma\", 40.0),\
            (\"Burtnīca\", 2.0)")
# Atjauninam vērtību datu bāzē
# https://www.sqlite.org/lang_update.html
cur.execute("UPDATE produkts SET piegadatajs = 1 WHERE id = 1")

cur.execute("CREATE TABLE IF NOT EXISTS piegadatajs (\
            id INTEGER UNIQUE,\
            nosaukums STRING,\
            adrese STRING,\
            telefonaNr STRING,\
            PRIMARY KEY (id AUTOINCREMENT)\
)")
# cur.execute("INSERT INTO piegadatajs (nosaukums, adrese, telefonanr) VALUES\
#             (\"AI Loģistika\", \"Nekuriene\", \"+00000-000\"),\
#             (\"CLV Loģistika\", \"LV\", \"+37100000000\")")
cur.close()
db.commit()
db.close()
