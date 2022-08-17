import random
import time

class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses = 0, kanal_listesi = ["Trt"], kanal = "trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("TV zaten açık!")
        else:
            print("TV açılıyor...")
            self.tv_durum = "Açık"
    
    def tv_kapat(self):
        if(self.tv_durum == "Kapalı"):
            print("TV zaten kapalı!")
        else:
            print("TV kapanıyor...")
            self.tv_durum = "Kapalı"
    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi Azalt: '<'\n Sesi Arttır '>'\nÇıkış: 'e'")
            if(cevap == '<'):
                if(self.tv_ses != 0):
                    self.tv_ses -=1
                    print("Ses", self.tv_ses)
            elif(cevap == '>'):
                if(self.tv_ses != 31):
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)
            else: 
                print("Ses Güncellendi: ", self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal Ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print(kanal_ismi , " Kanalı Eklendi...")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şuanki Kanal:" , self.kanal)
    def ___len___(self):
        return len(self.kanal_listesi)
    def ___str___(self):
        return "TV Durumu: {}\nTV Ses: {}\nKanal Listesi: {}\nŞuanki Kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()

print("""
    TV UYGULAMASI
    1. TV AÇ
    2. TV KAPAT
    3. SES AYARLARI
    4. KANAL EKLE
    5. KANAL SAYISI
    6. RASTGELE KANAL GEÇME
    7. TV BİLGİLERİ
Çıkmak için 'q' basın ...
""")

while(True):
    islem = input("İşlemi Seçiniz:")
    if(islem == "q"):
        print("Program Sonlandırılıyor...")
        break
    elif(islem == "1"):
        kumanda.tv_ac()
    elif(islem == "2"):
        kumanda.tv_kapat()
    elif(islem == "3"):
        kumanda.ses_ayarlari()
    elif(islem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin: ")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif(islem == "5"):
        print("Kanal Sayısı: ", len(kumanda))
    elif(islem == "6"):
        kumanda.rastgele_kanal()
    elif(islem == "7"):
        print(kumanda)
    else:
        print("Geçersiz İşlem !")