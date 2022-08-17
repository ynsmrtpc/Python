from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]
cift_sayilar = list(filter(lambda x : x % 2 == 0, liste))
toplam = reduce(lambda x,y : x + y, cift_sayilar)
print("Çift Sayılar: ", cift_sayilar)
print("Toplamı: ", toplam)