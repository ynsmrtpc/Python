liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
liste3 = ["Python","PHP","Java","JavaScript"]
# i = 0
# sonuc = list()
# while(i < len(liste1) and i < len(liste2)):
#     sonuc.append((liste1[i],liste2[i]))
#     i += 1
# print(sonuc)

print(list(zip(liste1,liste2)))
print(list(zip(liste1,liste2,liste3)))

print("-----------------------------------")

liste_1 = [1,2,3,4]
liste_2 = ["Python","PHP","Java","JavaScript"]

for i,j in zip(liste_1,liste_2):
    print(i,j)

print("-----------------------------------")

sozluk1 = {"Elma":1,"Armut":2,"Kiraz":3}
sozluk2 = {"Sıfır":0, "Bir":1, "İki":2}
print(list(zip(sozluk1,sozluk2)))
print(list(zip(sozluk1.values(),sozluk2.values())))
