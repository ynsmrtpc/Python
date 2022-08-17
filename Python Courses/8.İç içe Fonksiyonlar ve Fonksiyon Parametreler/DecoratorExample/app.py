def ekstra(func):
    def wrapper(sayilar):
        ciftler_toplami = 0
        cift_sayilar = 0
        tekler_toplami = 0
        tek_sayilar = 0
        for sayi in sayilar:
            if(sayi % 2 == 0):
                ciftler_toplami += sayi
                cift_sayilar += 1
            else:
                tekler_toplami += sayi
                tek_sayilar += 1
        print("Teklerin ortalamasi : " , tekler_toplami/tek_sayilar)
        print("Çiftlerin ortalamasi : " , ciftler_toplami/cift_sayilar)
        func(sayilar)
    return wrapper

@ekstra
def ortalamaBul(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    print("Genel Ortalama :", toplam/len(sayilar))

ortalamaBul([1,3,4,5,45,465,6,7,65,54,675,76,23])