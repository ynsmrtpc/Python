kenar_uzunlukları = [(3,4,5),(6,8,10),(3,10,7),(4,13,7),(5,12,13),(3,14,1)]

def ucgenMi(kenar):
    if(abs(kenar[0]+kenar[1]) > kenar[2] and abs(kenar[0]+kenar[2]) > kenar[1] and abs(kenar[1]+kenar[2]) > kenar[0]):
        return True
    else:
        return False
ucgenler = list(filter(ucgenMi,kenar_uzunlukları))
print("Üçgenlerin Kenar Uzunlukları: ", ucgenler)