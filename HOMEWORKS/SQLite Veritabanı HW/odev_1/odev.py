import sqlite3

class Sarki():
    def __init__(self,sarkiIsmi,sanatci,album,produksiyon,sure):
        self.sarkiIsmi = sarkiIsmi
        self.sanatci = sanatci
        self.album = album
        self.produksiyon = produksiyon
        self.sure = sure
    
    def __str__(self):
        return "Şarkı İsmi: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon Şirketi: {}\nSüre: {}\n".format(self.sarkiIsmi,self.sanatci,self.album,self.produksiyon,self.sure)
    
class Album():
    def __init__(self):
        self.baglantiOlustur()

    def baglantiOlustur(self):
        self.baglanti = sqlite3.connect("odev_1/sarkilar.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS sarkilar (Sarki_Ismi TEXT, Sanatci TEXT, Album TEXT,Produksiyon_Sirketi TEXT, Sarki_Suresi FLOAT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiKes(self):
        self.baglanti.close()

    def sarkiEkle(self, sarki):
        sorgu = "INSERT INTO sarkilar VALUES(?,?,?,?,?)"
        self.cursor.execute(sorgu, (sarki.sarkiIsmi, sarki.sanatci, sarki.album, sarki.produksiyon, sarki.sure))
        self.baglanti.commit()

    def sarkiSil(self, sarkiIsmi):
        sorgu = "DELETE FROM sarkilar WHERE sarkiIsmi = ?"
        self.cursor.execute(sorgu,(sarkiIsmi,))
        self.baglanti.commit()

    def toplamSure(self, sure):
        pass
