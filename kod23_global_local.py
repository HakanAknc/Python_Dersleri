a = 10 #global

def fonk():
    a = 5 #local değişkendir yukarıdaki a ile farklı ram adreslerinde saklanır
    print(a)

fonk()

b = 20 #global

def ikikati():
    global b
    b=5
    b *=6
    print(b)

ikikati()
