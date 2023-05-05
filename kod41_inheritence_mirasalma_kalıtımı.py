#Inheritence
#miras alma - kalıtım

class kus:
    tur_ad=""
    kus_ad=""
    def isimYaz(self):
        print("Tür adı :",self.tur_ad)
        print("Kuş ismi :",self.kus_ad)
class yirtici(kus):
    kanat_uzunlugu = "0"
    agirlik = "0"
class kartal(yirtici):
    alt_tur =""

