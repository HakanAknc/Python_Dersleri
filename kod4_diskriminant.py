import math

a = int(input("a sayısını giriniz: "))
b = int(input("b sayısını giriniz: "))
c = int(input("c sayısını giriniz: "))

delta = (b * b) - (4 * a * c)
print("Delta = " ,delta)

if delta>0:
    print("Denlemin iki farklı kökü vardır: ")
    kok1 = (-b+math.sqrt(delta)) / (2*a)
    print("kök1 = " ,kok1)
    kok2 = (-b-math.sqrt(delta)) / (2*a)
    print("kök2 = ", kok2)
elif delta==0:
    print("Denklemin çakışik iki kökü vardır: ")
    kok = -b/2*a
    print("kök1=kök2 = " ,kok)
else :
    print("Denklemin kökü yoktur")