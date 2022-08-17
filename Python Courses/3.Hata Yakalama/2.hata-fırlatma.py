# raise HataAdı (opsiyonel hata mesajı)

def tersCevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen string bir değer gönderin!")
    else:
        return s[::-1]
print(tersCevir("python"))
print(tersCevir(12))

# try: 
#     print(tersCevir(12))
# except ValueError:
#     print("Fonksiyon hata verdi!")