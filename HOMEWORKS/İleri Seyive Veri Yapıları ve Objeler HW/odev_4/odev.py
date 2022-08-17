isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Aleyna","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

tam_isim = list(zip(isimler,soyisimler))
tam_isim.sort()

for i,j in tam_isim:
    print(i,j)
