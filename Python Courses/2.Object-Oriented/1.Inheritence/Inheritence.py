class Calisan():
    def __init__(self,isim,maas,depertman):
        print("Çalışan sınıfının init fonksiyonu\n")
        self.isim = isim
        self.maas = maas
        self.depertman = depertman
    
    def bilgileriGoster(self):
        print("Çalışan sınıfının bilgileri ...\n")
        print("İsim: {}\nMaaş: {}\nDepertman: {}\n".format(self.isim,self.maas,self.depertman))
    
    def depertmanDegistir(self, yeni_depertman):
        self.depertman = yeni_depertman

class Yonetici(Calisan):
    # Overriding
    def __init__(self,isim,maas,depertman,kisi_sayisi):
        print("Yönetici sınıfının init fonksiyonu!\n")
        # self.isim = isim
        # self.maas = maas
        # self.depertman = depertman
        super().__init__(isim,maas,depertman)
        self.kisi_sayisi = kisi_sayisi

# Miras alındıktan sonra bir şeyler eklemek istersek tekrar aynı fonksiyonu yazabiliriz. Buna overriding denir.

    def zamYap(self, zam_miktari):
        self.maas += zam_miktari

    def bilgileriGoster(self):
        print("Yönetici sınıfının bilgileri ...\n")
        print("İsim: {}\nMaaş: {}\nDepertman: {}\nKişi Sayısı: {}\n".format(self.isim,self.maas,self.depertman,self.kisi_sayisi))

print("----------- ÇALIŞAN BİLGİLERİ --------------")
calisan = Calisan("Emre Topçu", 4500, "Bilişim")
calisan.bilgileriGoster()
print("----------- YÖNETİCİ BİLGİLERİ --------------")
yonetici = Yonetici("Yunus Topçu", 5000, "Yazılım",10)
yonetici.bilgileriGoster()
yonetici.depertmanDegistir("İnsan Kaynakları")
yonetici.zamYap(500)
yonetici.bilgileriGoster()