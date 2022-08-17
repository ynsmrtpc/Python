# BU PROGRAMI KOMUT SATIRINDAN ÇALIŞTIRMAK GEREKİR!
import sys
from types import WrapperDescriptorType

def kokBulma(a,b,c):
    delta = b ** 2 - 4 * a *c

    if delta < 0:
        print("Reel kök yoktur")

    else:
        x1 = (-b -delta ** 0.5) / (2*a)
        x2 = (-b +delta ** 0.5) / (2*a)
        return (x1,x2)

if len(sys.argv) == 4:
    print("Kök bulma: ",kokBulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))

else:
    sys.stderr.write("Lütfen doğru değerler giriniz!\n")
    sys.stderr.flush()