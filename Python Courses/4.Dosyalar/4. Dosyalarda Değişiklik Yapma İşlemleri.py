# with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/isimler.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/isimler.txt","r+",encoding="utf-8") as file:
#     file.seek(10)
#     file.write("Deneme")
#     print(file.read())

# DOSYANIN SONUNA EKLEME YAPMA
# with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/isimler.txt","a",encoding="utf-8") as file:
#     file.write("\nAleyna Kaya\n")

# DOSYANIN BAŞINA EKLEME YAPMA
# with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/isimler.txt","r+",encoding="utf-8") as file:
#     icerik = file.read()
#     icerik = "Hüsamettin Topçu\n" + icerik
#     file.seek(0)
#     file.write(icerik)
#     print(icerik) 

# DOSYANIN ORTASINA EKLEME YAPMA
with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/isimler.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    print(liste)
    liste.insert(1,"Müşerref Topçu\n")
    file.seek(0)
    for i in liste:
        file.write(i)

with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/isimler.txt","r+",encoding="utf-8") as file:
    liste2 = file.readlines()
    print(liste2)
    liste2.insert(3,"Bülent Topçu\n")
    file.seek(0)
    file.writelines(liste2)
    