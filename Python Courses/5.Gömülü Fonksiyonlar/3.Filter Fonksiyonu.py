# filter(fonksiyon, iterasyon yapılabilen veri tipi)
# birinci parametre olarak mutlaka mantıksal değer(True,False) dönen bir fonksiyon alır
# filter sadece True sonuç çıkaran değerleri alarak bir tane filter objesi döndürür.

print("Çift Sayılar:", list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8])))

def asalMi(x):
    i = 2
    if(x == 1):
        return False
    elif(x == 2):
        return True
    else:
        while(i < x):
            if(x % i == 0):
                return False
            i += 1
        return True

print("1'den 100'e Kadar Asal Sayılar:", list(filter(asalMi,range(0,100))))