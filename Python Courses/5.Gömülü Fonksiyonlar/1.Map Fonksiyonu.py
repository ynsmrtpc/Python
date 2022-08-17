# map(fonksiyon,iterasyon yapılabilecek veritipi(liste,demet vb.))
# def double(x):
#     return x * 2

# list1 = list(map(double,[1,2,3,4,5,6,7]))
# print(list1)


# print(list(map(lambda x : x ** 2, (1,2,3,4,5,6,7,8,9,10))))

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

print("İkisinin çarpımı: " , list(map(lambda x,y : x*y, liste1,liste2)))
print("Üçünün çarpımı: " , list(map(lambda x,y,z : x*y*z, liste1,liste2,liste3)))