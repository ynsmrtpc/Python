import sqlite3
con = sqlite3.connect("7.Sqlite Veritabanı/kutuphane.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT, Yazar TEXT, Yayinevi TEXT, Sayfa_Sayisi INT)")
    con.commit() # sorguyu çalıştırıp veritabanında tablo oluşturulmasını sağlar
# tablo_olustur()

def veri_ekle():
    cursor.execute("INSERT into kitaplik VALUES('İstanbul Hatırası', 'Ahmet Ümit', 'Everest', 561)")
    con.commit()
# veri_ekle()

def veri_ekle2(isim, yazar, yayinevi, sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(isim, yazar, yayinevi, sayfa_sayisi))
    con.commit()
# isim = input("İsim: ")
# yazar = input("Yazar: ")
# yayinevi = input("Yayınevi: ")
# sayfa_sayisi = int(input("Sayfa Sayısı: "))
# veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi)
def verileri_al():
    cursor.execute("SELECT * FROM kitaplik")
    liste = cursor.fetchall() # liste şeklinde işlem yaptığımız cursor'u bize döner
    print("\nKitaplık Tablosunun Bilgileri \n-----------------------------")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("SELECT Isim, Yazar FROM kitaplik")
    liste = cursor.fetchall()
    print("\nKitaplık Tablosunun Bilgileri \n-----------------------------")
    for i in liste:
        print(i)

def verileri_al3(yayinevi):
    cursor.execute("SELECT * FROM kitaplik WHERE Yayinevi = ?",(yayinevi,))
    liste = cursor.fetchall()
    print("\nKitaplık Tablosunun Bilgileri \n-----------------------------")
    for i in liste:
        print(i)
# verileri_al()
# verileri_al2()
# verileri_al3("Everest")

def verileri_guncelle(eski_yayinevi, yeni_yayinevi):
    cursor.execute("UPDATE kitaplik SET yayinevi = ? WHERE yayinevi = ?",(yeni_yayinevi,eski_yayinevi))
    con.commit()

# verileri_guncelle("Doğan Kitap", "Everest")
# verileri_al()

def verileri_sil(yazar):
    cursor.execute("DELETE FROM kitaplik WHERE yazar = ?",(yazar,))
    con.commit()

verileri_sil("Ahmet Ümit")
verileri_al()


con.close()