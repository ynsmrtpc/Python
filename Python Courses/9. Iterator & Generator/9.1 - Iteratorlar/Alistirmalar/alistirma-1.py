class kupAl():
    def __init__(self, finish = 0):
        self.finish = finish
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.finish:
            result = self.n ** 3
            self.n += 1
            return result
        else:
            raise StopIteration
sayi  = 5
sayilar = kupAl(sayi)
i = iter(sayilar)

j = 1
while(True):
    try:
        if sayi >= j:
            print("{}. Adım:".format(j), next(sayilar))
            j += 1
        else:
            print("Çözüm:", next(sayilar) )
    except StopIteration:
        break
        print("Çözüm sona erdi!")