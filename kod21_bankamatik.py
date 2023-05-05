#Banka ATM
banknot = [200,100,50,20,10]
para = int(input("Çekmek istediğiniz para miktarını giriniz:"))
while True:
    if para%10==0:
        for i in range(len(banknot)):
            if para >=banknot[i]:
                banknotadet = int(para / banknot[i])
                para = para % banknot[i]
                print(banknotadet,"adet",banknot[i])
        else:
             break
    else:

         print("Lütfen onun katında bir değer giriniz!")
         para = int(input("Para miktarını giriniz:"))
