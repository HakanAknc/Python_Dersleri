toplam = 0
sayac = 0

for i in range(100):
    if i%3==0:
        toplam = toplam + i
        sayac = sayac + 1
ort = toplam / sayac
print("Toplam =" ,toplam)
print("3'e bölünen sayı adedi =",sayac)
print("ortalama =" ,ort)

print("*************************")

toplam = sayac = 0
for i in range(100):
    if i%5==0:
        toplam+=i
        sayac+=1
ort = toplam / sayac
print("Toplam =",toplam)
print("5'e bölünen sayı adedi =",sayac)
print("ortalama =",ort)
