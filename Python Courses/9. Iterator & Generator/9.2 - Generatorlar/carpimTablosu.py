def carpimTablosu():
    for i in range(1,11):
        for j in range(1,11):
            if j == 10:
                yield "{} x {} = {}".format(i,j,i*j)
                print("\n-----------------------\n")

            else:
                yield "{} x {}  = {}".format(i,j,i*j)

for i in carpimTablosu():
    print(i)

x = input()