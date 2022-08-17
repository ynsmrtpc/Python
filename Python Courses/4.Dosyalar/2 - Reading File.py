# file = open("bilgiler2.txt", "r")

# try:
#     file = open("bilgiler2.txt", "r")
# except FileNotFoundError:
#     print("Dosya Bulunamadı!")

# file = open("bilgiler.txt","r",encoding="utf-8")
# for i in file:
#     print(i, end = "")
# file.close()

file = open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/bilgiler.txt","r",encoding="utf-8")

icerik = file.read()
print("Dosyanın İçeriği\n",icerik)

icerik2 = file.read()
print("Dosyanın İçeriği-2\n",icerik2)
file.close()
print("--------------------------------")
file = open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/bilgiler.txt","r",encoding="utf-8")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline()) # okunacak bir şey kalmazsa boşluk yazdırır
file.close()
print("--------------------------------")

file = open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/bilgiler.txt","r",encoding="utf-8")
liste = file.readlines()
print(liste)
file.close()