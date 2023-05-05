kume = {1,5,0,3,4,7,7,3,0}

#kümelerde tekrar eden eleman olmaz
#kümeler (set) verileri otomatik sıralar

print(kume)

sk ={"ali","veli","ayşe","hüsyin","zeynep"}
print(sk)

A = {3,1,0,8,9,7,4}
B = {2,0,8,7,5,6,1}

#A-B fark almak
fark = A.difference(B)
print(fark)

#AUB birleşim
birlesim = A.union(B)
print(birlesim)

#AnB kesişim
kesisim = A.intersection(B)
print(kesisim)

dizi = [2,1,1,2,4,3,6,7,6]
sd = set(dizi)
print(sd)

s = "bugün hava çok güzel"
print(set(s))
