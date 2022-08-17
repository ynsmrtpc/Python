with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/İleri Seyive Veri Yapıları ve Objeler HW/odev_3/mailler.txt","r",encoding="utf-8") as file:
    mailler = file.read()
    mail_tutucu = mailler.split()
    for i in mail_tutucu:
        if(i.endswith(".com") and (i.find("@") != -1)):
            print(i)

#  ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ HATALI ÇÖZÜM  ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
#     mailler = file.read()
#     mail_tutucu = mailler.split()

# for i in mail_tutucu:
#     if((i.endswith("gmail.com") == True) or (i.endswith("yahoo.com")) == True or (i.endswith("hotmail.com") == True)):
#         print(i)
