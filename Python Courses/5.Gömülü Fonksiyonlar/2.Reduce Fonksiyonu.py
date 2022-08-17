# reduce fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular ve daha sonra çıkan
# sonucu listenin 3. elemanına uygular ve bu şekilde devam ederek liste bitince bir tane değer döner.
# reduce(fonksiyon,iterasyon yapılabilen veritipi(liste,vb))

from functools import reduce
from tkinter.constants import X

def toplama(x,y):
    return x+y

print("Toplam: ", reduce(toplama,[12,18,20,10]))

print("Faktoriyel: ", reduce(lambda x,y : x*y, [1,2,3,4,5]))

def maksimum(x,y):
    if(x>y):
        return x
    else:
        return y

print("Maksimum Değer: ", reduce(maksimum,[-2,3,1,4,6,5]))