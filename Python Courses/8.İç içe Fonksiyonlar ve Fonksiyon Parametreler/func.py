# def function(*args):
#     for i in args:
#         print(i)
# print("--------------------")
# function("Yunus","Emre","Topçu")
# print("--------------------")
# function(0,1,2,3,4,5,6,7,8,9,10)

def fonksiyon(**kwarsg):
    print(kwarsg)

fonksiyon(isim = "Yunus", soyisim = "Topçu", numara = 251)

def func(**kwargs):
    for i,j in kwargs.items():
        print("Argüman ismi: ", i, ", Argüman Değeri: " , j)

func(isim = "Yunus", soyisim = "Topçu", numara = 251)

print("--------------------")

def fonksiyon(*args, **kwargs):
    for i in args:
        print(i)
    print("--------------------")
    for i,j in kwargs.items():
        print(i,j)
    
fonksiyon(1,2,3,4,5,6,isim = "Yunus", soyisim = "Topçu", no = 251)
fonksiyon(23,43,54,67,43,34,isim = "Aleyna", soyisim = "Kaya", no = 123)