with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/Dosyalar/odev_2/futbolcular.txt","r",encoding="utf-8") as file:
    fb = list()
    gs = list()
    bjk = list()

    for satir in file:
        satir = satir[:-1]
        liste = satir.split(",")
        futbolcu = liste[0]
        if(liste[1] == "Fenerbahçe"):
            fb.append(futbolcu + "\n")
        elif(liste[1] == "Galatasaray"):
            gs.append(futbolcu + "\n")
        elif(liste[1] == "Beşiktaş"):
            bjk.append(futbolcu + "\n")
    
    with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/Dosyalar/odev_2/fb.txt","w",encoding="utf-8") as file1:
        for i in fb:
            file1.write(i)
    with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/Dosyalar/odev_2/gs.txt","w",encoding="utf-8") as file1:
        for i in gs:
            file1.write(i)
    with open("/Volumes/GoogleDrive/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Projects_HW/Dosyalar/odev_2/bjk.txt","w",encoding="utf-8") as file1:
        for i in bjk:
            file1.write(i)
            