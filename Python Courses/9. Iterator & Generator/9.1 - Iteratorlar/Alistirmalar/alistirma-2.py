class SonsuzIter:
    'Çift sayıları döndüren bir iterator'
 
    def __iter__(self):
        self.i = 0
        return self
 
    def __next__(self):
        self.i += 2
        return self.i
 
a = iter(SonsuzIter())
for i in a:
    print(i)