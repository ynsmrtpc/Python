def anafonksiyon(islem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi == "toplama":
        return toplama
    else:
        return carpim

fonk = anafonksiyon("toplama")
fonk2 = anafonksiyon("carpim")

print("Toplam: " , fonk(1,2,3,4,5,6,7,8))
print("Çarpim: " , fonk2(1,2,3,4,5))

def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b
print("------------------------------------")
def mainFunction(func1,func2,func3,func4,islem_adi):
    if islem_adi == "toplama":
        print("Toplam :" , func1(3,4))
    elif islem_adi == "cikarma":
        print("Fark :", func2(10,3))
    elif islem_adi == "carpma":
        print("Carpim :", func3(3,5))
    elif islem_adi == "bolme":
        print("Bolum :", func4(10,4))
    else:
        print("Gecersiz islem!")

mainFunction(toplama,cikarma,carpma,bolme,"toplama")
mainFunction(toplama,cikarma,carpma,bolme,"cikarma")
mainFunction(toplama,cikarma,carpma,bolme,"carpma")
mainFunction(toplama,cikarma,carpma,bolme,"bolme")