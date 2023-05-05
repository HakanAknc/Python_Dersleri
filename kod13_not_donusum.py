v = int(input("Vize notununzu giriniz: "))
f = int(input("Final notunuzu giriniz: "))

o = (v * 0.4) + (f * 0.6)

if o>=90 and o<=100:
    print("AA")
elif o>=85 and o<=89:
    print("BA")
elif o>=75 and o<=84:
    print("BB")
elif o>=70 and o<=74:
    print("CB")
elif o>=60 and o<=69:
    print("CC")
elif o>=55 and o<=59:
    print("DC")
elif o>=50 and o<=54:
    print("DD")
elif o>=40 and o<=49:
    print("FD")
elif o>=0 and o<=39:
    print("FF")

