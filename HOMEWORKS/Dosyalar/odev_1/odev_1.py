# notları hesaplayıp harf notlarını çıkarır
def not_hesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim  = liste[0]
    not_1 = int(liste[1])
    not_2 = int(liste[2])
    not_3 = int(liste[3])
    son_not = not_1 * 0.3 + not_2 * 0.3 + not_3 * 0.4

    if (son_not >= 90):
        harf = " AA"
    elif (son_not >= 85):
        harf = " BA"
    elif (son_not >= 80):
        harf = " BB"
    elif (son_not >= 75):
        harf = " CB"
    elif (son_not >= 70):
        harf = " CC"
    elif (son_not >= 65):
        harf = " DC"
    elif (son_not >= 60):
        harf = " DD"
    elif (son_not >= 55):
        harf = " FD"
    else:
        harf = " FF"

    return isim + " -->" + harf +"\n"

# notlara göre geçme kalma durumunu sağlar
def gecme_kalma_durumu(satır):
    satır = satır[:-1]
    liste = satır.split("-->")
    isim  = liste[0]
    harf_notu = liste[1]

    if(harf_notu == " FF"):
        durum = " KALDI"
    elif(harf_notu == " FD"):
        durum = " SORUMLU GEÇTİ"
    else:
        durum = " GEÇTİ"
    return isim + "-->" + durum + "\n"

# notlar.txt dosyası oluşturup isimlerin karşısına harf notlarını yazdırma
with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/Dosyalar/odev_1/dosya.txt","r",encoding="utf-8") as file: # Mac  
    eklenecekler_listesi = []   
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))
    print(eklenecekler_listesi)
with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/Dosyalar/odev_1/notlar.txt","w",encoding="utf-8") as file2: #Mac
    for i in eklenecekler_listesi:
        file2.write(i)

# gecenler.txt dosyası oluşturup geçme kalma durumunu isimlerin karşısına yazdırır
with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/Dosyalar/odev_1/notlar.txt","r",encoding="utf-8") as file3: # Mac
    gecenlerin_listesi = []
    for i in file3:
        gecenlerin_listesi.append(gecme_kalma_durumu(i))
    print(gecenlerin_listesi)

with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/Dosyalar/odev_1/gecme-kalma.txt","w",encoding="utf-8") as file4: #Mac
    for i in gecenlerin_listesi:
        file4.write(i)


