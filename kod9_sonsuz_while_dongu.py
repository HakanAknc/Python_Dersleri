# kullanıcıyı 0 - 100 arası sayı girmeye zorlayacağız

v = int(input("Lütfen 0 ile 100 arasında bir sayı giriniz:"))

while True: #sonsuz döngüsü
    if v>=0 and v<=100:
        break  # 0-100 arasında ise döngüyü kırıryoruz
    else:
        print("Lütfen 0 -100 aralığında bir sayı giriniz!")
        v = int(input("Lütfen 0 ile 100 arasında bir sayı giriniz:"))

#final alıyoruz
f = int(input("Lütfen 0 ile 100 arasında bir sayı giriniz:"))

while True: #sonsuz döngü
    if f>=0 and f<=100:
        break  # 0-100 arasında ise döngüyü kırıryoruz
    else:
        print("Lütfen 0 - 100 aralığnda girirniz!")
        f = int(input("Lütfen 0 ile 100 arasında bir sayı giriniz:"))

ort = v*0.4 + f*0.6
print("Ortalama =",ort)
