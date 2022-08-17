# Listeyi Numaralandırır

liste = ["Elma", "Armut", "Muz", "Kiraz"]

print(list(enumerate(liste)))
print("-----------------------------------")

for i,j in enumerate(liste):
    print(i,j)

print("-----------------------------------")

liste2 = ["a","b","c","d","e","f","g"]
for index,eleman in enumerate(liste2):
    if(index % 2 == 0):
        print("Eleman:", eleman)