from datetime import date, datetime
import locale
from time import time # türkçe yapmak için

locale.setlocale(locale.LC_ALL,"tr") # bölgemizi Türkiye olarak ayaladık

suan = datetime.now()  # şuanki tarihi ve zamanı alır
print("{} yılının {} ayının {} günündeyiz. Saat ise {}:{}:{}".format(suan.year,suan.month,suan.day,suan.hour,suan.minute,suan.second))
print("- - - - - - - - - - - - - - - ")
print(datetime.ctime(suan))
print("- - - - - - - - - - - - - - - ")
print("yıl: ",datetime.strftime(suan,"%Y"))
print("ay: ",datetime.strftime(suan,"%B"))
print("gün", datetime.strftime(suan,"%D"))
print("ay-yıl:", datetime.strftime(suan,"%B %Y"))
print("- - - - - - - - - - - - - - - ")

# çevirimler
saniye = datetime.timestamp(suan) # içinde bulunulan azmanı saniyeye çevirdik
suan2 = datetime.fromtimestamp(saniye)
print("saniye: ",saniye)
print(suan2)
print("- - - - - - - - - - - - - - - ")
milat = datetime.fromtimestamp(0)
print("epoch time:", milat)
print("- - - - - - - - - - - - - - - ")
tarih = datetime(2022,7,1)
bugün = datetime.now()
print("Mezun olmama {} gün kaldı.".format(tarih-bugün))
print("- - - - - - - - - - - - - - - ")
