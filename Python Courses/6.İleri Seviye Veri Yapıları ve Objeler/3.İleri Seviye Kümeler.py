# x = {1,2,3}
# print(type(x))
# y = set()
# print(type(y))
# print("-----------------------")

# liste = [1,2,3,3,1,1,2,2,2]
# l = set(liste)
# print(l)
# print("-----------------------")

# s = set("Python Programlama Dili")
# print(s)
# print("-----------------------")

# k = {"Python", "Php", "Python"}
# print(k)
# print("-----------------------")

# t = {"Elma","Armut","Kiraz","Muz"}
# for i in t:
#     print(i)
# print("-----------------------")

# # Kümelerin indeksi olmaz

# p = {"Python", "Php", "Java", "JavaScript"}
# liste2 = list (p)
# print(liste2)
# for i in liste2:
#     print(i)
# print("-----------------------")
print("-----------------------")
# kümelerde ekleme işlemi 
x = {1,2,3,4,5}
x.add(5)
# Kümelerde aynı eleman 2 kere bulunamaz
x.add(6) # ekleme işlemi 
print("-----------------------")
# kümelerin farklarını bulma işlemi
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
print(kume1.difference(kume2))
print(kume2.difference(kume1))
print("-----------------------")
# difference_update() - s1. Kümenin 2. Kümeden farkını döner ve belirtilen kümeyi bu farka göre günceller
kume1.difference_update(kume2)
print("Kume1: ", kume1, "\nKume2: ", kume2)
print("-----------------------")
# discard() - kümeden eleman çıkarmak
k = {1,2,3,4,5,6,}
print(k)
k.discard(3)
k.discard(100) # eğer kümede bu eleman bulunmuyorsa hiç bir şey olmaz, hata vermez
print(k)
print("-----------------------")
# intersection() - ortak elemanları bulmaya yarar 
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
print("Ortak Elemanlar:", kume1.intersection(kume2))
# intersection_update() - kesişim kümesini belirtilen kümeye atar
print("1.Küme: ", kume1, "\n2.Küme: ", kume2)
kume1.intersection_update(kume2)
print("-----intersection_update()-------")
print("1.Küme: ", kume1, "\n2.Küme: ", kume2)
print("-----------------------")
# isdisjoint() - ayrık küme olup olmadığı true ya da false olarak bize bildirir
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
kume3 = {90,80,70}
print("kume1 ve kume2: ", kume1.isdisjoint(kume2))
print("kume1 ve kume3: ", kume1.isdisjoint(kume3))
print("-----------------------")
# issubset() - alt kümesi mi?
kume_1 = {1,2,3}
kume_2 = {1,2,3,4}
kume_3 = {5,6,7}
print("1.küme 2.kümenin alt kümesi mi? ", kume_1.issubset(kume_2))
print("1.küme 3.kümenin alt kümesi mi? ", kume_1.issubset(kume_3))
print("-----------------------")
# union() - iki kümenini birleşim kümesini oluşturur
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
print("1.Küme: ", kume1, "\n2.Küme: ", kume2)
print("birleşim kümesi: ", kume1.union(kume2))
# update() - 1. kümeye 2. kümenin birleşim kümesini döner ve birinci kümeyi buna göre günceller
print("------update()--------")
kume1.update(kume2)
print("kume1: ", kume1)
print("-----------------------")