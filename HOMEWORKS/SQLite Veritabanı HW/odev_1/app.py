from odev import *

print("""
\n**********************************
ŞARKI SORGULAMA PROGRAMINA HOŞGELDİNİZ ! 

1. Şarkı Ekle
2. Şarkı Sil
3. Toplam Şarkı Süresini Hesapla

Çıkmak için 'q' ya basınız...
***********************************\n
""")

album = Album()

while(True):
    islem = input("Yapacağınız işlemi giriniz: ")
    if(islem == "q"):
        print("Program Sonlandırılıyor...")
        break
    elif(islem == "1"):
        sarkiIsmi = input("Şarkı İsmi: ")
        sanatci = input("Sanatçı: ")
        album = input("Albüm: ")
        produksiyon = input("Prodüksiyon Şirketi: ")
        sure = float(input("Süre: "))
        yeniSarki = Sarki(sarkiIsmi,sanatci,album,produksiyon,sure)
        album.sarkiEkle(yeniSarki)
        print("Şarkı başarıyla eklendi!")
    elif(islem == "2"):
        sarkiIsmi = input("Hangi Şarkıyı Sİlmek İstiyorsunuz: ")
        album.sarkiSil(sarkiIsmi)
        print("Şarkı başarıyla silindi!")
