liste = [1,2,3,4,5]

iterator = iter(liste)
print(iterator)

print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3
print(next(iterator)) # 4
print(next(iterator)) # 5
# print(next(iterator)) # StopIteration hatası alırız.
print("----------------------------------")

# for döngüsü iterator'dan oluşur

list1 = [1,2,3,4,5,6,7,8,9,10]
iterator1 = iter(list1)
# for i in list1:
#     print(i)
while(True):
    try:
        print(next(iterator1))
    except StopIteration:
        break
print("----------------------------------")

class Kumanda():
    def __init__(self,kanalListesi):
        self.kanalListesi = kanalListesi
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index < len(self.kanalListesi):
            return self.kanalListesi[self.index]
        else:
            self.index = -1
            raise StopIteration

kumanda = Kumanda(["STAR","ATV","TRT","FOX","Kanal D", "Bloomberg"])
iterator2 = iter(kumanda)

# i = 1
# while(True):
#     try:
#         print("{}.Kanal".format(i) , next(iterator2))
#         i += 1
#     except StopIteration:
#         print("StopIteration Error! / Daha fazla eleman yok!")
#         b reak

j = 1
for i in kumanda:
    print("{}.Kanal: ".format(j), i)
    j += 1

