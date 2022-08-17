import random
import time

print("""
SAYI TAHMİN OYUNU

1 ile 40 Arasında Bir sayı Tahmin Edin

3 Tahmin Hakkınız Olduğunu Unutmayın!
""")
# print("Öncelikle sayının hangi aralıkta olduğunu belirleyin ↓")
# sayi_1 = 1
# sayi_2 = int(input("Sayınız birden başlar ve bu aralığa kadar gider:"))
rastgele_sayi = random.randint(1,40)
tahmin_hakki = 3
while True:
    tahmin = int(input("Tahmininiz:"))
    if(tahmin < rastgele_sayi):
        print("Kontrol sağlanıyor...")
        time.sleep(1)
        print("Yukarı!")
        tahmin_hakki -= 1
    elif(tahmin > rastgele_sayi):
        print("Kontrol sağlanıyor...")
        time.sleep(1)
        print("Aşağı!")
        tahmin_hakki -=1
    else:
        print("Kontrol sağlanıyor...")
        time.sleep(1)
        print("Tebrikler! ", rastgele_sayi, "sayısını doğru tahmin ettiniz!")
        break
    if (tahmin_hakki == 1):
        print("Son 1 Hakkınız Kaldı!")
    elif(tahmin_hakki == 0):
        print("Tahmin Hakkınız Bitti...")
        print("Sayı:", rastgele_sayi)
        break