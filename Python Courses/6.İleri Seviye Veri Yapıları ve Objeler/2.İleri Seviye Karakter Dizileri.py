# upper() - stringin tüm karakterlerini büyük harfe çevirir
# lower() - stringin tüm karakterlerini küçük harfe çevirir

print("python".upper())
print("PYTHON".lower())
print("-----------------------")
# replace() - stringde belirlediğimiz harfi belirttiğimiz harf ile değiştirir
print("Herkes ana baba bacı gardaş".replace("a","o"))
print("Python Programlama Dili".replace(" ","-"))
print("Kunduz".replace("duz","zun"))
print("-----------------------")
# startswith(x), endswith(x) - x ile başlıyorsa veva bitiyorsa TRUE, başlamıyor veya bitmiyorsa FALSE döndürür
print("Pyton".startswith("Py"))
print("Pyton".endswith("Py"))
print("-----------------------")
# strip(), lstrip(), rstrip() - sırasıyla başından ve sonundan, başından, sonundan değerleri siler
print("             python               ".strip(" "))
print("             python               ".lstrip(" "))
print("             python               ".rstrip(" "))
print("-----------------------")
# join() - listenin elemanlarını bir string değeriyle birleştirmeye yarar
liste = ["23","10","2021"]
print("/".join(liste))
liste2 = ["T","B","M","M"]
print(".".join(liste2))
print("-----------------------")
# count(x) - stringin içindeki x değerlerini sayar
# count(x,index) - stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar
print("ada kapısı yandan çarklı".count("a"))
print("ada kapısı yandan çarklı".count(" "))
print("ada kapısı yandan çarklı".count("a",2))
print("-----------------------")
# find(x) - x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi, bulamazsa -1'i döndürür.
# rfind(x) - x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi, bulamazsa -1'i döndürür.
print("araba".find("a"))
print("araba".rfind("a"))
print("araba".find("s"))
print("-----------------------")