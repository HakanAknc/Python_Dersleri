# faktoriyel çözümü

def faktoriyel(n):
    if n==0 or n==1:
        return 1
    else:
        return  n * faktoriyel(n-1)  #5 * 4 * 3 * 2 * 1

print(faktoriyel(5))

print("**********************")

#recursive ornek

dizi = [4,2,5]   #dizi=[3]

def diziToplam(dizi):
    if len(dizi) == 1:
        return dizi[0]
    else:
        return dizi[0] * diziToplam(dizi[1:])

print(diziToplam(dizi))
