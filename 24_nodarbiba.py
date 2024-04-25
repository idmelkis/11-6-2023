# Risinājums - skat. grafiku šai nodarbībai.
# import sqlite3
# db = sqlite3.connect('24_nodarbiba.db')
# cur = db.cursor()

# # Ieslēdzam foreign key atbalstu datu bāzē
# cur.execute("PRAGMA foreign_keys = ON;")

# cur.execute("CREATE TABLE IF NOT EXISTS autors (\
#             id INTEGER UNIQUE,\
#             lietotajvards STRING,\
#             parole STRING,\
#             epasts STRING,\
#             PRIMARY KEY (id AUTOINCREMENT)\
# )")

# cur.execute("CREATE TABLE IF NOT EXISTS ieraksts (\
#             id INTEGER UNIQUE,\
#             autors INTEGER,\
#             nosaukums STRING,\
#             teksts STRING,\
#             izveidots STRING,\
#             redzams integer,\
#             PRIMARY KEY (id AUTOINCREMENT),\
#             FOREIGN KEY(autors) REFERENCES autors(id) ON DELETE CASCADE\
# )")

# cur.execute("CREATE TABLE IF NOT EXISTS komentars (\
#             id INTEGER UNIQUE,\
#             ieraksts INTEGER,\
#             autors STRING,\
#             teksts STRING,\
#             redzams integer,\
#             PRIMARY KEY (id AUTOINCREMENT),\
#             FOREIGN KEY(ieraksts) REFERENCES ieraksts(id) ON DELETE CASCADE\
# )")

# cur.execute("INSERT INTO autors (lietotajvards, parole, epasts) VALUES\
#             ('admin', 'parole', 'admin@mail.com'),\
#             ('user', 'parole123', 'user@mail.com')")
# cur.execute("INSERT INTO ieraksts (autors, nosaukums, teksts, redzams) VALUES\
#             (1, 'sveika pasaule', ':)', 1),\
#             (2, 'Otrais raksts', ':X', 0)")
# cur.execute("INSERT INTO komentars (ieraksts, autors, teksts, redzams) VALUES\
#             (1, 'Janis', 'Sveiks!', 1),\
#             (1, 'spam', 'buy coin', 0),\
#             (2, 'user', 'Test', 1)")

# cur.close()
# db.commit()
# db.close()

# Datu ieguve:
# Datu bāzes lejupielādes links:
# https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip
import sqlite3
db = sqlite3.connect('C:\\Users\\idmelkis\\Downloads\\chinook\\chinook.db')
cur = db.cursor()

# 1. Uzdevums
# Iegūt no tabulas "employees" visus cilvēku vārdus, 
# uzvārdus un e-pastus (LastName, FirstName, Email)
# cur.execute("SELECT FirstName, LastName, Email FROM employees")
# print(cur.fetchall())
# cur.execute("SELECT * FROM employees")
# results = cur.fetchall()
# for result in results:
#     print(f"{result[2]} {result[1]} {result[14]}")


# 2. Uzdevums: Iegūt māksliniekus/grupas
# no tabulas "artists" kurām nosaukumā ir vārds "Black"
# Grupu nosaukumi ir kolonā "Name" (tādas ir 5). Izmantot op. LIKE
cur.execute("SELECT Name FROM artists WHERE Name LIKE \"%Black%\"")
print(cur.fetchall())


# 3. Uzdevums
# Izvadat no tabulas "customers" informāciju par to cik klienti 
# ir noteiktam atbalsta personālam
# Personāla ID tiek glabāts kolonā (SupportRepId).
# Saskaitīšanai izmantot funkciju COUNT, grupēt ar GROUP BY.
cur.execute('SELECT SupportRepId, COUNT(*) FROM customers GROUP BY SupportRepId')
print(cur.fetchall())

# 4. Uzdevums
# Iegūt pirmos 3 ierakstus no tabulas "invoice_items".
# Kur (InvoiceID) ir 3.
# cur.execute("SELECT * FROM invoice_items WHERE InvoiceID = 3 LIMIT 3")
# print(cur.fetchall())
# cur.execute("SELECT * FROM invoice_items WHERE InvoiceID = 3")
# print(cur.fetchmany(3))

cur.close()
db.close()

# Pēdiņās ir tabulu nosaukumi, iekavās ir kolonu nosaukumi.
# Uzrakstīt vaicājumus kas ļauj iegūt sekojošus datus:
# Dati tiek iegūti no Chinook datu bāzes: http://s.ayy.lv/chnk

# 1. No tabulas "invoices" izvadīt pirmos 5 rēķinus 
# kas ir izrakstīti (BillingCountry) vācijā
# un kuru summa (Total) ir virs 1.00. Izmantojat AND.
# 2. Noteikt cik dziesmām tabulā "tracks" cena (UnitPrice) ir 0.99
# Var veikt programmiski -- iegūstam vērtības no tabulas un saskaitam iekš 
# python, vai var veikt ar vaicājumu: COUNT(*) + GROUP BY.
# 3. (nav obligāti, bet ja ātrāk pabeidzāt varat pamēģināt)
# Tabulā "albums" noteikt grupu/mākslinieku albumam ar id (AlbumId) 141.
# Mākslinieka ID šajā tabulā tiek glabāts kolonā (ArtistID).
# Mākslinieku informācija tiek glabāti tabulā "artists", kur 
#    ID lauks ir (ArtistID) un 
#    grupas nos. ir kolonā (Name)
