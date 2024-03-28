# 1. Uzdevums
# Nolasiet datus no dotā faila 
# Formāts
# {'date': {'year': 2024, 'date': 25, 'month': 03}, ...}
# Un saglabājiet tos vārdnīcā.
# Izvadat šo vārdnīcu
# Piezīmes: 
# 1. Izmantojat .split() funckiju
# 2. Lai atrastu noteiktu simbola pozīciju tekstā var izmantot
# <string>.index('<simbols>') funkciju, 
# kas atgriež simbola pozīciju
# Github links: https://s.ayy.lv/11-6
# vardnica = {}
# with open('20_nodarbiba.ini', 'r', encoding='utf-8') as f:
#     virsraksts = ""
#     for line in f:
#         if line.startswith("["):
#             virsraksts = line[line.index("[") + 1 : line.index("]")]
#             vardnica[virsraksts] = {}
#         elif line.strip() == "":
#             continue
#         else:
#             vertiba = line.split("=")
#             vardnica[virsraksts][vertiba[0].strip()] = vertiba[1].strip()
# print(vardnica)

# import configparser
# from pathlib import Path
# fails = "20_nodarbiba.ini"
# parser1 = configparser.ConfigParser()
# parser1.read(Path(fails))
# print(parser1.sections())
# print(parser1['date']['month'])

# parser2 = configparser.ConfigParser()
# parser2['kaut_kas'] = {}
# parser2['kaut_kas']['kaut_kas_cits'] = "-9"
# parser2['kaut_kas']['kaut_kas_cits2'] = "-9"
# with open('20_nodarbiba_.ini', 'w') as f:
#     parser2.write(f)

# 2. Uzdevums
class Gene:
    HGNC :str
    Symb :str
    Name :str
    Ens  :str = ""
    def __init__(self, hgnc, symb, name) -> None:
        self.HGNC = hgnc
        self.Symb = symb
        self.Name = name
    def __str__(self) -> str:
        return f"{self.Symb}: {self.Name} -- {self.Ens}"

# Slikta ideja - lādējot otro failu jāiet pāri visam sarakstam
# Tās ir ~ 50 000 * 50 000 iterācijas. Uz skolas datoriem tas prasīs
# Aptuveni 5min.
# geni = []
genu_vardn = {}
with open('20nodarbiba_uzd\\genenames_filtered.txt', 'r', encoding='utf-8') as f:
    next(f)
    for line in f:
        dati = line.split('\t')
        gens = Gene(dati[0].strip(), dati[1].strip(), dati[2].strip())
        genu_vardn[dati[1].strip()] = gens
        #geni.append(gens)

with open('20nodarbiba_uzd\\mart_export_human_filtered.txt', 'r', encoding='utf-8') as f:
    next(f)
    for line in f:
        dati = line.split('\t')
        # for gens in geni:
        #     if gens.Symb == dati[1].strip():
        #         gens.Ens = dati[0].strip()
        if dati[1].strip() in genu_vardn:
            genu_vardn[dati[1].strip()].Ens = dati[0].strip()
        
# for gens in geni:
#     print(gens)
for value in genu_vardn.values():
    print(value)

# DBMS: https://en.wikipedia.org/wiki/Database
# ACID: https://en.wikipedia.org/wiki/ACID
# Relational DB: https://en.wikipedia.org/wiki/Relational_database
# SQL: https://en.wikipedia.org/wiki/SQL
# SQLite: https://www.sqlite.org/
# SQLite DB Browser: https://sqlitebrowser.org/
#import sqlite3