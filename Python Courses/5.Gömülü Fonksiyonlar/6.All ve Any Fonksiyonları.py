# def hepsi(liste):
#     for i in liste:
#         if not i:
#             return False
#     return True
# liste = [True,False,True,False,True]
# print(hepsi(liste))
# liste2 = [1,2,3,4,5]
# print(hepsi(liste2))
# print("-----------------------------------")

# def herhangi(liste):
#     for i in liste:
#         if i:
#             return True
#     return False

# print(herhangi(liste))
# liste3 = [0,0,0,0,0,0,0,0]
# print(herhangi(liste3))

liste = [True,False,True,False,True]
print(all(liste)) # all fonksiyonu hepsi true ise true geri kalan durumlarda false verir
print(any(liste)) # en az 1 tane true varsa true verir, hepsi false ise false verir