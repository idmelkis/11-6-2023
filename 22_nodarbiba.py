import sqlite3

db = sqlite3.connect('22_nodarbiba.db')
cur = db.cursor()

#cur.execute("DROP TABLE atzime")
# cur.execute("CREATE TABLE IF NOT EXISTS atzime ( \
#             id INTEGER NOT NULL UNIQUE,\
#             skolens INTEGER,\
#             atzime INTEGER,\
#             prieksmets TEXT,\
#             PRIMARY KEY(id AUTOINCREMENT)\
# )")

# for i in range(0, 10):
#     cur.execute(f"INSERT INTO atzime (atzime) VALUES ({i})")

# Iegūt tikai noteiktas kolonas
# cur.execute("SELECT id, atzime FROM atzime")
# results = cur.fetchall()
# print(results)

# https://www.sqlite.org/lang_expr.html#operators_and_parse_affecting_attributes
# https://www.sqlitetutorial.net/sqlite-where/
# = - vienādojums
# != - negatīvs vienādojums
# <> - negatīvs vienādojums
# LIKE - Teksta salīdzinājums
# > - lielāks par
# < - mazāks par
### value > 5 AND value < 10 - apvienojat salīdzinājumus ar AND.
# BETWEEN <vērtība1> AND <vērtība2> - starp noteiktām vērtībām
# Vaicājumus var apvienot ar AND, OR utt.

# cur.execute("SELECT * FROM atzime WHERE atzime = 5")
# results = cur.fetchall()
# print(results)

# Teksta meklēšana
# cur.execute("SELECT * FROM atzime WHERE prieksmets LIKE \"Mat%\"")
# results = cur.fetchall()
# print(results)

# Diapazons
# cur.execute("SELECT * FROM atzime WHERE atzime > 5 AND atzime < 9")
# results = cur.fetchall()
# print(results)
# cur.execute("SELECT * FROM atzime WHERE atzime BETWEEN 6 AND 8")
# results = cur.fetchall()
# print(results)

# Maksimālā vērtība, vēl ir min utt.
# cur.execute("SELECT id, max(atzime) FROM atzime")
# results = cur.fetchall()
# print(results)

# Sakārtošana (DESC - dilstošā, ASC - augošā)
# cur.execute("SELECT id, atzime FROM atzime\
#     ORDER BY atzime ASC, id DESC")
# results = cur.fetchall()
# print(results)

# cur.execute("SELECT id, atzime FROM atzime LIMIT 5")
# results = cur.fetchall()
# print(results)

# Apvienojam filtrus
# cur.execute("SELECT id, atzime FROM atzime\
#             WHERE atzime > 5\
#             ORDER BY atzime DESC\
#             LIMIT 5")
# results = cur.fetchall()
# print(results)

# Foreign key
# https://www.sqlite.org/foreignkeys.html
# Ieslēgt foreign key atbalstu
cur.execute("PRAGMA foreign_keys = ON;")
cur.execute("CREATE TABLE IF NOT EXISTS skolens (\
            id INTEGER NOT NULL UNIQUE,\
            vards TEXT,\
            PRIMARY KEY(id AUTOINCREMENT)\
)")
#cur.execute("DROP TABLE atzime")
cur.execute("CREATE TABLE IF NOT EXISTS atzime (\
            id INTEGER NOT NULL UNIQUE,\
            skolens INTEGER,\
            atzime INTEGER,\
            prieksmets TEXT,\
            PRIMARY KEY(id AUTOINCREMENT),\
            FOREIGN KEY(skolens) REFERENCES skolens(id) ON DELETE RESTRICT\
)")
# ON DELETE RESTRICT - Neļaut dzēst
# ON DELETE CASCADE - Izdzēst visas saistītās vērtības
# ON DELETE DO NOTHING...

# cur.execute("INSERT INTO skolens (vards) VALUES (\"Janis\"), (\"Peteris\")")
# cur.execute("INSERT INTO atzime (skolens, atzime) VALUES (1, 9), (2, 3)")
# https://www.sqlite.org/lang_delete.html
cur.execute("DELETE FROM skolens WHERE id = 1")

cur.close()
db.commit()
db.close()
