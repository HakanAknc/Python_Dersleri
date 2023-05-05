#İsmini ekrana 50 kere yazdır

isim = input("İsminizi giriniz: ")

for i in range(50):    ##range() fonksiyonu belirli aralıkta bulunan sayıları göstermek için kullanılır.
    print(i,"Hakan")   #range(100) fonksiyonu, 100'e kadar olan sayıları yani 0,1,2,3,4........ değerlerini ifade eder.

print("*******************")

#0'dan 100'e kadar olan sayıların toplamı

toplam = 0

for i in range(100):
    toplam = toplam + i     #toplam += i
    #print(toplam)  eğer bu şekilde yazılırsa for bloğunun içide tüm ara toplamlar yazılır
print(toplam)