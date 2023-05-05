#sayı tahmin oyunu #bilgisayar sayı tutuyor
import random
sayi = random.randint(0,100)
sayac = 0
tahmin = int(input("0 ile 100 arasında bir sayı tahmin ediniz: "))

while tahmin != sayi:
    sayac = sayac + 1
    if sayac==10:
        print("Hakkınız bitti.")
        break
    if sayi>tahmin:
        print("YUKARI")
        tahmin = int(input("Bir sayı tahmin ediniz: "))
    else:
        print("AŞAĞI")
        tahmin = int(input("Bir sayı tahmin ediniz: "))

if sayac<10:
    print("Tebrikler" ,sayac, "denemede bildiniz")