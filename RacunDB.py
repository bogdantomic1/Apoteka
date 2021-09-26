import sqlite3

class Racun:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS racun (id INTEGER PRIMARY KEY, naziv TEXT, cena INT, kolicina INT)")
        self.conn.commit()

    def pokupi(self, naziv=''):
        self.cur.execute(
            "SELECT * FROM racun WHERE naziv LIKE ?", ('%'+naziv+'%',))
        redovi = self.cur.fetchall()
        return redovi


    def ubaci(self, naziv, cena, kolicina):
        self.cur.execute("INSERT INTO racun VALUES (NULL, ?, ?, ?)", (naziv, cena, kolicina))
        self.conn.commit()

    def izbrisi(self, id):
        self.cur.execute("DELETE FROM racun WHERE id=?", (id,))
        self.conn.commit()

    def azuriraj(self, id, naziv, cena, kolicina):
        self.cur.execute("UPDATE racun SET naziv = ?, cena = ?, kolicina = ? WHERE id = ?",
                         (naziv, cena, kolicina, id))
        self.conn.commit()
    def stampaj(self):
        self.cur.execute("SELECT * from racun")
        redovi = self.cur.fetchall()
        return redovi
    def obrisi(self):
        self.cur.execute("DELETE FROM racun ")
        self.conn.commit()

    def __del__(self):
        self.conn.close()
