bas_harfler = ""
with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/İleri Seyive Veri Yapıları ve Objeler HW/odev_2/siir.txt","r",encoding="utf-8") as file:
    siir = file.read()
    poem = siir.replace(" ", "")
    
with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/İleri Seyive Veri Yapıları ve Objeler HW/odev_2/siir.txt","w",encoding="utf-8") as file2:
    file2.write(poem)

with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/İleri Seyive Veri Yapıları ve Objeler HW/odev_2/siir.txt","r",encoding="utf-8") as file3:
    for satir in file3:
        bas_harfler += satir[0]
print(bas_harfler)