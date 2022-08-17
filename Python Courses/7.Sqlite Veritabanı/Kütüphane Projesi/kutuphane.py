import sqlite3
import time

class Kitap():
    def __init__(self, isim, yazar, yayinevi, tur, baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):
        return "Kitap İsmi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)
    
class Kutuphane():
    def __init__(self):
        self.baglantiOlustur()
    def baglantiOlustur(self):
        self.baglanti = sqlite3.connect("Python Courses/7.Sqlite Veritabanı/Kütüphane Projesi/kutuphane.db")
        #self.baglanti = sqlite3.connect("kutuphane.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar (Isim TEXT, Yazar TEXT, Yayınevi TEXT, Tur TEXT, Baski INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    
    def baglantiyiKes(self):
        self.baglanti.close()
    
    def kitaplariGoster(self):
        sorgu = "SELECT * FROM kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
    
    def kitapSorgula(self, isim):
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor...")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)
        
    def kitapEkle(self, kitap):
        sorgu = "INSERT INTO kitaplar VALUES(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim, kitap.yazar, kitap.yayinevi, kitap.tur,kitap.baski))
        self.baglanti.commit()
    
    def kitapSil(self,isim):
        sorgu = "DELETE FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu, (isim,))
        self.baglanti.commit()
    
    def baskiYukselt(self,isim):
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor...")
        else:
            baski = kitaplar[0][4]
            baski += 1
            sorgu2 = "UPDATE kitaplar SET baski = ? WHERE isim = ?"
            self.cursor.execute(sorgu2, (baski,isim))
            self.baglanti.commit()
