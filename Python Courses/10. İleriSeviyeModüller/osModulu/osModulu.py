import os
from datetime import date,datetime

# print(dir(os))

os.chdir("G:\Diğer bilgisayarlar\DELL - Windows\Çalışma Dosyaları\PYTHON\Python Courses\İleri Seviye Modüller\osModulu") # içine yazdığımız konuma gider
print("Konum: ",os.getcwd()) # bulunduğumuz dizini söyler

for i in os.listdir(): # olduğumuz dizindeki klasör ve dosyaları listeler, yazdırır
    print(i)

# Klasör Oluşturma

os.mkdir("deneme1") # tek bi klasör oluşturmak için
os.makedirs("deneme2/deneme3") # iç içe oluşturmak için

# İsim Değiştirme

#os.rename("test.txt,"test2.txt)

x = input("silmek için 'enter' basınız...")
print("- - - - - - - - - - - - - - - ")

# Klasör Silme
os.rmdir("deneme1")
os.removedirs("deneme2/deneme3")
print("- - - - - - - - - - - - - - - ")

print(os.stat("osModulu.py"))
degistirmeZamani = datetime.fromtimestamp(os.stat("osModulu.py").st_mtime)
print("Dosyanın en son değiştirilme zamanı: ", degistirmeZamani)

print("- - - - - - - - - - - - - - - ")

for klasorYolu,klasorIsimleri,dosyaIsimleri in os.walk("C:/Users/Lenovo/Desktop"):
    print("Klasör Yolu:",klasorYolu)
    print("Klasör İsimleri:",klasorIsimleri)
    print("Dosya İsimleri:",dosyaIsimleri)
    print("- - - - - - - - - - - - - - - ")

    # for i in klasorIsimleri:
    #     print(i)

    # for i in dosyaIsimleri:
    #     if(i.endswith(".txt")):
    #         print(i)

