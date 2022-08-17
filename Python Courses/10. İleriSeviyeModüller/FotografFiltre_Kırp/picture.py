from PIL import Image, ImageFilter

image = Image.open("g:/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Python Courses/10. İleriSeviyeModüller/FotografFiltre_Kırp/kus/kus.jpg")
# image.show() #fotografi acar

# kaydetme
image.save("g:/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Python Courses/10. İleriSeviyeModüller/FotografFiltre_Kırp/kus/kus2.jpg")

# döndürme
image.rotate(180).save("g:/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Python Courses/10. İleriSeviyeModüller/FotografFiltre_Kırp/kus/kus3.jpg")

# siyah-beyaz
image.convert(mode="L").save("g:/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Python Courses/10. İleriSeviyeModüller/FotografFiltre_Kırp/kus/kus5.jpg")

# boyut degistirme
resize = (960,600)
image.thumbnail(resize)
image.save("g:/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Python Courses/10. İleriSeviyeModüller/FotografFiltre_Kırp/kus/kus6.jpg")

image.filter(ImageFilter.GaussianBlur(5)).save("g:/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Python Courses/10. İleriSeviyeModüller/FotografFiltre_Kırp/kus/kus7.jpg")
image.filter(ImageFilter.GaussianBlur(10)).save("g:/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Python Courses/10. İleriSeviyeModüller/FotografFiltre_Kırp/kus/kus8.jpg")


image2 = Image.open("g:/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Python Courses/10. İleriSeviyeModüller/FotografFiltre_Kırp/ataturk/ataturk.jpg")
kirpilacak_alan = (340,0,950,600)

image2.crop(kirpilacak_alan).save("g:/Diğer bilgisayarlar/DELL - Windows/Çalışma Dosyaları/PYTHON/Python Courses/10. İleriSeviyeModüller/FotografFiltre_Kırp/ataturk/ataturk2.jpg")
