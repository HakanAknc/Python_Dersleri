# ASCII

print(chr(65))
print(ord("A"))

print(chr(97))
print(ord("h"))

import random
s = ""
for i in range(5): #rastgele 5 harfli string üretelim
    s += chr(random.randint(65,90))

print(s)

print("***************")

#kullancıdan büyük harf ingiliz alfabesi ile
#ismini alıp
#ismindeki harflerin karşılığını fonksiyon ile bulalım

isim = input("Adını gir aslan parçası:")

def asciDonusum(isim):
    for i in isim:
        print(ord(i),"-")

asciDonusum(isim)
