# bir fonksiyon def ön eki ile tanımlanır
# fonksiyonları programın üstüne yazmayı alışkanlık edinelim

def hosgeldin(): #parametre almayan fonksiyon
    print("Hoşgeldiniz kardeşlerim")

hosgeldin() #fonksiyonu ana satırdan çağırıyoruz
hosgeldin()
hosgeldin()
hosgeldin()

def merhaba(isim): #fonksiyon parametre alıyor
    print("aferin",isim)

isim = input("ismini gir aslan parçası:")
merhaba(isim)

def carp(x,y):
    return x*y

print(carp(5,9))
