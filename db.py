import sqlite3

class Baza:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS lek (id INTEGER PRIMARY KEY, naziv TEXT, proizvodjac TEXT, cena INT, stanje INT)")
        self.conn.commit()

    def pokupi1(self, naziv=''):
        self.cur.execute(
            "SELECT * FROM lek WHERE naziv LIKE ?", ('%'+naziv+'%',))
        redovi = self.cur.fetchall()
        return redovi

    
    def stampaj(self):
        self.cur.execute("SELECT * from lek")
        redovi2 = self.cur.fetchall()
        return redovi2




    def ubaci(self, naziv, proizvodjac, cena, stanje):
        self.cur.execute("INSERT INTO lek VALUES (NULL, ?, ?, ?, ?)", (naziv, proizvodjac, cena, stanje))
        self.conn.commit()

    def izbrisi(self, id):
        self.cur.execute("DELETE FROM lek WHERE id=?", (id,))
        self.conn.commit()

    def azuriraj(self, id, naziv, proizvodjac, cena, stanje):
        self.cur.execute("UPDATE lek SET naziv = ?, proizvodjac = ? \t, cena = ?, stanje = ? WHERE id = ?",
                         (naziv, proizvodjac, cena, stanje, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

