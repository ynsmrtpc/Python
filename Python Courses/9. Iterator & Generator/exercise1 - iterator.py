class kuvvet3():
    def __init__(self,max = 0):
        self.max = max
        self.kuvvet = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.kuvvet <= self.max:
            sonuc = 3 ** self.kuvvet
            self.kuvvet += 1
            return sonuc
        else:
            self.kuvvet = 0 # ikinci kez for döngüsüyle çağırabilmek için bu şekilde yaptık.
            raise StopIteration

kuvvet = kuvvet3(6)
i = iter(kuvvet)

for j in kuvvet:
    print(j)
print("--------------")
for k in kuvvet:
    print(k)