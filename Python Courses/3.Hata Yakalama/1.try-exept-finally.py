# try:
#     Hata Çıkabilecek Kodlar Buraya Yazılır!
#     Eğer hata çıkarsa program uygun olan except bloğuna girer
#     Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmaz

# except Hata1:
#     Hata1 oluştuğunda burası çalışır
# except Hata2:
#     Hata2 oluştuğunda burası çalışır

import os

def clear():
    os.system('clear')

print("\n")

try:
    a = int("sadsfasdsaf23423535")
    print("Program Burada")
except ValueError:
    print("Bir hata oluştu!")
print("Bloglar Sona Erdi")

print("\n")

try:
    b = int("34")
    print("Program Burada")
except:
    print("Bir hata oluştu!")
print("Bloglar Sona Erdi\n")

clear()

try: 
    a = int(input("Sayi1:"))
    b = int(input("Sayi2:"))
    print(a/b)
except ValueError:
    print("Lütfen inputu doğru girin")
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez")

# İki hatayı aynı except bloğunda yazabiliriz !

clear()

try: 
    a = int(input("Sayi1(birleşik blok):"))
    b = int(input("Sayi2(birleşik blok):"))
    print(a/b)
except (ValueError, ZeroDivisionError):
    print("Lütfen inputu doğru girin")
    print("Bir sayı sıfıra bölünemez")

clear()

# finally blokları mutlaka çalışır !

try: 
    a = int(input("Sayi1:"))
    b = int(input("Sayi2:"))
    print(a/b)
except ValueError:
    print("Lütfen inputu doğru girin")
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez")
finally: # bu blok hata olması durumunda da hata olmaması durumunda da çalışır! 
    print("Burası çalıştı!")