kenar_uzunluklari = [(3,4),(10,3),(5,6),(1,9)]

def dik_alan(kenar):
        return kenar[0] * kenar[1]

alan = list(map(dik_alan,kenar_uzunluklari))
print("Alanlar: ", alan)