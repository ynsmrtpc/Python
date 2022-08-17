from kutuphane import *

print("""
***********************************
KÜTÜPHANE PROGRAMINA HOŞGELDİNİZ ! 

1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt
Çıkmak için 'q' ya basınız...
***********************************
""")

kutuphane = Kutuphane()

while(True):
    islem = input("Yapacağınız işlemi giriniz:")
    if(islem == "q"):
        print("Program Sonlandırılıyor...")
        break
    elif(islem == "1"):
        kutuphane.kitaplariGoster()
    elif(islem == "2"):
        isim = input("Kitap İsmini Girin:")
        print("Kitap sorgulanıyor...")
        time.sleep(1)
        kutuphane.kitapSorgula(isim)
    elif(islem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayinevi = input("Yayınevi:")
        tur = input("Tür:")
        baski = int(input("Baskı:"))
        yeniKitap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap ekleniyor...")
        time.sleep(1)
        kutuphane.kitapEkle(yeniKitap)
        print("Kitap başarıyla eklendi!")
    elif(islem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz:")
        cevap = input("Emin Misiniz? (e/h)")
        if(cevap == "e"):
            print("Kitap Siliniyor...")
            time.sleep(1)
            kutuphane.kitapSil(isim)
            print("Kitap başarıyla silindi!")
    elif(islem == "5"):
        isim = input("Kitap İsmi:")
        print("Baskı yükseltiliyor...")
        time.sleep(1)
        kutuphane.baskiYukselt(isim)
        print("{} isimli kitap {}. baskıdan {}. baskıya başarıyla yükseltildi!".format(isim,baski,baski+1))      
    else:
        print("Geçersiz İşlem...")
        