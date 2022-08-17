def not_hesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim  = liste[0]
    not_1 = int(liste[1])
    not_2 = int(liste[2])
    not_3 = int(liste[3])
    son_not = not_1 * 0.3 + not_2 * 0.3 + not_3 * 0.4

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + " -->" + harf +"\n"

# with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/Not Hesaplama Sistemi/dosya.txt","r",encoding="utf-8") as file: # Mac
with open("C:\Users\Emre\Desktop\⠀\Çalışma Dosyaları\PYTHON\ 4.Dosyalar\Not Hesaplama Sistemi\dosya.txt","r",encoding="utf-8") as file: # Windows
    
    eklenecekler_listesi = []
    
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))
    print(eklenecekler_listesi)

# with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/4.Dosyalar/Not Hesaplama Sistemi/notlar.txt","w",encoding="utf-8") as file2: #Mac
with open("C:\Users\Emre\Desktop\⠀\Çalışma Dosyaları\PYTHON\ 4.Dosyalar\Not Hesaplama Sistemi\ notlar.txt","w",encoding="utf-8") as file2:    #Windows
    for i in eklenecekler_listesi:
        file2.write(i)
