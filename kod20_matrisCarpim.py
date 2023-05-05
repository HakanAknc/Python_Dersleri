#İki adet random oluşturulan 3x3 matrislerin çarpımı


import random

m1 = [[0 for x in range(3)] for y in range(3)]
m2 = [[0 for x in range(3)] for y in range(3)]
mc = [[0 for x in range(3)] for y in range(3)]

for i in range(3):
    for j in range(3):
        m1[i][j] = random.randint(0,4)
        m2[i][j] = random.randint(0,4)

for i in range(3):
    for j in range(3):
        for k in range(3):
            mc[i][j] += m1[i][k] * m2[k][j]

print("1.matris")
for i in range(3):
    print(m1[i])

print("2.matris")
for i in range(3):
    print(m2[i])

print("Matrisleri Çarpımı")
for i in range(3):
    print(mc[i])
