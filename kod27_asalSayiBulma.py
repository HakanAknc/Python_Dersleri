#kendisine gönderilen sayı asal ise true değilse false döndüren bir fonksiyon yazınız

def asalMi(s):
    bolensayac=0
    for i in range(2,s):
        if s%i==0:
            bolensayac+=1
    if bolensayac>0:
        return False
    else:
        return True
s = int(input("Hele bi sayı gir:"))
if asalMi(s):
    print("Girdiğin sayı ASAL.")
else:
    print("Girdiğin sayı ASAL değil.")
