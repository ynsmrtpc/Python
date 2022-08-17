#     Dosyaların Otomatik Kapanması
# with open(dosyaAdı,dosyaKipi) as file:
#     Dosya İşlemleri

# with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/bilgiler.txt", "r", encoding="utf-8") as file:
#     print(file.tell())

# with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/bilgiler.txt", "r", encoding="utf-8") as file:
#     file.seek(20)
#     print(file.tell())


with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/bilgiler.txt", "r", encoding="utf-8") as file:
    file.seek(5) # dosya içerisinde 5. satıra geldik
    icerik = file.read(10) # bulunduğumuz konumdan(5.satır) itibaren 10 icerik değişkenine atadık
    print(icerik) # icerik değişkeninin ekrana yazdırdık (n,Java,C,P)
    print(file.tell()) # nerede bulunduğumuzu ekrana yazdırdık (15)
    file.seek(0) # 0. satıra geri döndük
    icerik2 = file.read(6) # 0. satırdan itibaren 6 satır icerik2 değişkeninin içine attık
    print(icerik2) # icerik 2 değişkenini ekrana yazdırdık (Python)