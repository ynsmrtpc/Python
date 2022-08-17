import math
import os
import time
    
def clear():
    os.system('cls')
    os.system('clear')

while(True):
    clear()
    print("""
    Seçiminizi Yapın

    1. Toplama
    2. Çıkarma
    3. Çarpma
    4. Bölme
    5. Kalan Bulma
    0. Gelişmiş Mod
    """)
    secim = int(input("Seciminiz:"))
    if (secim == 1):
        sayi1 = int(input("1. Sayiyi Girin: "))
        sayi2 = int(input("2. Sayiyi Girin: "))
        print("Toplam:" , sayi1 + sayi2)
        time.sleep(1)
    if (secim == 2):
        sayi1 = int(input("1. Sayiyi Girin: "))
        sayi2 = int(input("2. Sayiyi Girin: "))
        print("Fark:" , sayi1 - sayi2)
        time.sleep(1)
    if (secim == 3):
        sayi1 = int(input("1. Sayiyi Girin: "))
        sayi2 = int(input("2. Sayiyi Girin: "))
        print("Çarpım:" , sayi1 * sayi2)
        time.sleep(1)
    if (secim == 4):
        sayi1 = int(input("1. Sayiyi Girin: "))
        sayi2 = int(input("2. Sayiyi Girin: "))
        print("Bölüm:" , sayi1 / sayi2)
        time.sleep(1)
    if (secim == 5):
        sayi1 = int(input("1. Sayiyi Girin: "))
        sayi2 = int(input("2. Sayiyi Girin: "))
        print("Kalan:" , sayi1 % sayi2)
        time.sleep(1)
    if (secim == 0):
        clear()
        print("""
        Gelişmiş Mod'a Hoşgeldiniz !
        Yapmak İstediğiniz İşlemi Aşağıdan Seçiniz

        1. Faktoriyel
        2. Mutlak Değer Alma
        3. EBOB Bulma
        4. e Sabitini Ekrana Yazdırma
        5. pi Sayısını Ekrana Yazdırma
        6. Logaritma Hesabı 
        7. Üs Hesabı
        8. Karekök Hesabı
        """)
        secim2 = int(input("Seçiminiz: "))
        if (secim2 == 1):
            sayi = int(input("Sayiyi Girin: "))
            print("Faktoriyel: " , math.factorial(sayi))
            time.sleep(1)
        if (secim2 == 2):
            sayi = int(input("Sayiyi Girin: "))
            print("Mutlak Değer: " , math.fabs(sayi))
            time.sleep(1)
        if (secim2 == 3):
            sayi1 = int(input("1. Sayiyi Girin: "))
            sayi2 = int(input("2. Sayiyi Girin: "))
            sayi3 = int(input("3.Sayiyi Girin: "))
            print("EBOB: ", math.gcd(sayi1,sayi2,sayi3))
            time.sleep(1)
        if (secim2 == 4):
            print("e Sabiti: " , math.e)
            time.sleep(1)
        if (secim2 == 5):
            print("pi Sayısı: " , math.pi)
            time.sleep(1)
        if (secim2 == 6):
            sayi1 = int(input("1. Sayiyi Girin: "))
            sayi2 = int(input("2. Sayiyi Girin: "))
            print("1. Sayının 2. Sayıya Göre Logaritması: " , math.log(sayi1,sayi2))
            time.sleep(1)
        if (secim2 == 7):
            sayi1 = int(input("1. Sayiyi Girin: "))
            sayi2 = int(input("2. Sayiyi Girin: "))
            print("1. Sayının 2. Sayıya Göre Kuvveti: ", math.pow(sayi1,sayi2))
            time.sleep(1)
        if (secim2 == 8):
            sayi = int(input("Sayiyi Girin: "))
            print("Karekök: " , math.sqrt(sayi))
            time.sleep(1)