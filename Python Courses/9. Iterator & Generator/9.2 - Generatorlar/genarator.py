# Genarator Kullanmadan

# def kareleriAl():
#     sonuc = []

#     for i in range(1,6):
#         sonuc.append(i ** 2)
#     return sonuc

# print(kareleriAl())


def kareleriAl():
    for i in range(1,6):
        yield i ** 2

generator = kareleriAl()
print(generator) # genarator objesini oluşturduğumuzu ekrana yazdırdık

iterator = iter(generator)

for i in iterator:
    print(i)

iterator2 = iter(generator)
# print(next(iterator2)) # hata alırız çünkü, generator'lar değerleri 1 kere üretirler ve yok ederler. üretilen bir değer
                         # geri dönüşümlü olarak tekrar kullanılamaz