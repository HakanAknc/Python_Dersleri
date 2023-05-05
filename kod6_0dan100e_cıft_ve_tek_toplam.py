#Çift sayıların toplamı...
toplam = 0

for i in range(100):
    if(i % 2 == 0):   #Çift sayı mood alma
        toplam = toplam + i
print("Çift sayıların toplamı: " ,toplam)

#Tek sayıların toplamı...
toplam = 0

for i in range(100):
    if(i % 2 == 1):   #Tek sayı mood alma
        toplam = toplam + i
print("Tek sayıları toplamı: " ,toplam)

print("**********************")
#25'den 55'e beşer beşer artırma
for i in range(25,55,5):
    print(i)

print("*********************")
#10'dan 40'a kadar ikişer ikişer artırma
for i in range(10,40,2):
    print(i)

print("*********************")
#0'dan 10'a kadar birer birer artırma
for i in range(10):
    print(i)

print("*********************")
#10'dan 60'a kadar artırma
for i in(10,20,30,40,50,60):
    print(i)

print("**********************")
#ismimizi tek tek yazar
for i in "HAKANNN":
    print(i)