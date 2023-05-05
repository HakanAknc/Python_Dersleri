#kendisine gönderilen 3 sayının çarpımını return eden fonksiyon

def carpim(a,b,c):
    return a*b*c
a = int(input("a sayısı:"))
b = int(input("b sayısı:"))
c = int(input("c sayısı:"))
print(carpim(a,b,c))


h = int(input("Birinci sayıyı giriniz:"))
k = int(input("İkinci sayıyı giriniz:"))
n = int(input("Üçüncü sayıyı giriniz:"))

C = h * k * n

def diziToplam(C):
    return print("SONUÇ =",C)

diziToplam(C)
