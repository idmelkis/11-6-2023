# Uzdevums:
# Izveidot datu bāzi kas glabās informāciju par CSN pārkāpumu sodiem
# 1. Tabula - Pārkāpējs [ ID, Vārds, Uzvārds, PersKods ]
# 2. Tabula - Sods [ ID, Pants, SodaPunkti, NaudasSods, Datums, Pārkāpējs (Pārkāpējs.ID) ]

# import sqlite3
# db = sqlite3.connect('25_nodarbiba.db')
# cur = db.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS parkapejs (\
#             id INTEGER UNIQUE,\
#             vards STRING,\
#             uzvards STRING,\
#             perskods INTEGER,\
#             PRIMARY KEY (id AUTOINCREMENT)\
# )")

# # Datums - 
# # 1. variants - UNIX laiks (INTEGER, sekundes no 1970. gada 1. janv)
# # 2. variants - 2024. gada 2. maijs 09:12:00.000
# cur.execute("PRAGMA foreign_keys = ON;")
# cur.execute("CREATE TABLE IF NOT EXISTS sods (\
#             id INTEGER UNIQUE,\
#             pants STRING,\
#             punkti INTEGER,\
#             sods FLOAT,\
#             datums INTEGER,\
#             parkapejs INTEGER,\
#             PRIMARY KEY (id AUTOINCREMENT),\
#             FOREIGN KEY (parkapejs) REFERENCES parkapejs(id)\
# )")

# cur.close()
# db.commit()
# db.close()

# Uzdevums: Izveidot mapi output, saglabāt failu ar lietotāja dotu nosaukumu,
# kurš satur pašreizējo laiku
# Pašreizējais laiks UNIX formātā:
# import time
# laiks = int(time.time())
# import os

# if not os.path.exists("output"):
#     os.mkdir("output")

# nosaukums = input('Nosaukums: ')
# # TODO: Pārbaudīt vai nav liegtie simboli (:!@...)
# import time
# with open(f'output\\{nosaukums}', 'w') as f:
#     f.writelines(str(int(time.time())))

# Uzdevums: (\t - tab poga uz klaviatūras!!!!)
# Doti 2 faili
# Fails 1:
# ID\tVards\tUzvards
# 1\tJanis\tEgle
# 2\tSamanta\tPriede

# Fails2
# Datums\tPircejaID
# 1111\t1
# 1115\t2
# 1113\t1

# Atvērt abus failus, un izvadīt datus sekojošā formātā
# Pircējs {Vārds} {Uzvārds} Veica pirkumus datumos:
# {Datums1}
# ...
class Pircejs:
    def __init__(self, vards, uzvards) -> None:
        self.vards = vards
        self.uzvards = uzvards
        self.datumi = []
    def add_time(self, time) -> None:
        self.datumi.append(time)
dati = {} # id: Pircejs
with open('25_nodarbiba_f1.txt', 'r') as f:
    next(f)
    for line in f:
        parsedLine = line.split('\t')
        dati[parsedLine[0].strip()] = Pircejs(parsedLine[1].strip(), parsedLine[2].strip())
with open('25_nodarbiba_f2.txt', 'r') as f:
    next(f)
    for line in f:
        parsedLine = line.split('\t')
        dati[parsedLine[1].strip()].add_time(parsedLine[0].strip())
        # pircejs = dati[parsedLine[1]]
        # pircejs.add_time(...)

for key, value in dati.items():
    print(f"Pircējs {value.vards} {value.uzvards} veica pirkumus datumos:")
    for date in value.datumi:
        print(date)

# Uzdevums: Ievietot šos datus datu bāzē, saistīt tabulas (foreign key)

# 1. Izveidojat tabulas ar kolonām no šiem failiem (CREATE TABLE ...)
# 2. Ielādējat datus no faila (with open...)
# 3. Ievietojat datu bāzē (INSERT ...)