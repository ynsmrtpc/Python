print("-----------------------")
# extend() - bir listeye başka bir listenin elemanlarını eklemaye yarar
liste1 = [1,2,3,4,4,5,6,7]
liste2 = [10,20,30]
print("liste1: ", liste1, "\tliste2: ", liste2)
liste1.extend(liste2)
print("liste1 updated: ", liste1)
print("-----------------------")
# instert() - belirlediğimiz indekse eleman eklememizi sağlar
liste = [1,2,3,4,4,5,6,7]
print("liste: ", liste)
liste.insert(2,"Python")
liste.insert(0, "Java")
print("liste updated: ", liste)
print("-----------------------")
# pop() - eleman siler
liste = [1,2,3,4,5,6,7]
liste.pop(3) # 3. indeksteki elemanı siler
liste.pop() # sondaki elemanı siler
print("liste updated: (3. ve sonuncu indeks silindi)", liste)
print("-----------------------")
# remove() - içine elemanın adını yazarız o şekilde siler, olmayan bir elemanı yazarsak hata verir
liste = [1,2,3,4,5,6,7]
liste.remove(2)
liste.remove(1)
print("liste updated: (2 ve 1 silindi)", liste)
print("-----------------------")
# index() - verilen elemanın indeksini döndürür
liste = [1,2,3,4,3,3,5,6,7,8,9]
print("3 elemanı hangi index'te: ", liste.index(3))
print("3 elemanı hangi index'te: ", liste.index(3,3)) # 3.index'ten itibaren aramaya başla ve 3 değerini ara
print("-----------------------")
# sort() - elemanları sayı ise küçükten büyüğe, string ise alfabetik olarak sıralar. Eğer içine reverse=True değeri verilirse
# elemanları büyükten küçüğe sıralar
liste = [12,-2,3,1,34,100]
liste.sort()
print("Küçükten büyüğe: ", liste)
liste.sort(reverse=True)
print("Büyükten Küçüğe: ", liste)
liste = ["Python", "C", "Java", "Php"]
liste.sort()
print("Alfabetik olarak: ",liste)
liste.sort(reverse=True)
print("Alfabenin tersinden başlayarak: ", liste)
print("-----------------------")
