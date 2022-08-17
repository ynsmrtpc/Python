with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/İleri Seyive Veri Yapıları ve Objeler HW/odev_1/kelime.txt","r",encoding="utf-8") as file:
    harfler = file.read()

harf_sozluk = dict()
for i in harfler:
    if(i in harf_sozluk):
        harf_sozluk[i] += 1
    else:
        harf_sozluk[i] = 1

for harf,sayi in harf_sozluk.items():
    print("{} harfi, {} defa geçiyor !".format(harf,sayi))