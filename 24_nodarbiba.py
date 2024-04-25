import sqlite3
db = sqlite3.connect('24_nodarbiba.db')
cur = db.cursor()

# Ieslēdzam foreign key atbalstu datu bāzē
cur.execute("PRAGMA foreign_keys = ON;")

cur.execute("CREATE TABLE IF NOT EXISTS autors (\
            id INTEGER UNIQUE,\
            lietotajvards STRING,\
            parole STRING,\
            epasts STRING,\
            PRIMARY KEY (id AUTOINCREMENT)\
)")

cur.execute("CREATE TABLE IF NOT EXISTS ieraksts (\
            id INTEGER UNIQUE,\
            autors INTEGER,\
            nosaukums STRING,\
            teksts STRING,\
            izveidots STRING,\
            redzams integer,\
            PRIMARY KEY (id AUTOINCREMENT),\
            FOREIGN KEY(autors) REFERENCES autors(id) ON DELETE CASCADE\
)")

cur.execute("CREATE TABLE IF NOT EXISTS komentars (\
            id INTEGER UNIQUE,\
            ieraksts INTEGER,\
            autors STRING,\
            teksts STRING,\
            redzams integer,\
            PRIMARY KEY (id AUTOINCREMENT),\
            FOREIGN KEY(ieraksts) REFERENCES ieraksts(id) ON DELETE CASCADE\
)")

cur.execute("INSERT INTO autors (lietotajvards, parole, epasts) VALUES\
            ('admin', 'parole', 'admin@mail.com'),\
            ('user', 'parole123', 'user@mail.com')")
cur.execute("INSERT INTO ieraksts (autors, nosaukums, teksts, redzams) VALUES\
            (1, 'sveika pasaule', ':)', 1),\
            (2, 'Otrais raksts', ':X', 0)")
cur.execute("INSERT INTO komentars (ieraksts, autors, teksts, redzams) VALUES\
            (1, 'Janis', 'Sveiks!', 1),\
            (1, 'spam', 'buy coin', 0),\
            (2, 'user', 'Test', 1)")

cur.close()
db.commit()
db.close()