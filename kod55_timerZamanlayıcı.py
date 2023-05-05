#Timer - Zamanlayıcı

import time
from tkinter import *

#from i in range(30,0,-1)
    #print(i)
    #time.sleep(0.1)  # 1000 ms = 1 sn   --> sleep komutu saniye cinsinden  # 0.1 = 100 ms

pencere = Tk()
pencere.geometry("300x300")
i = 0
def yaz():
    global i
    i+=1
    #I['text']=str(i) labelin text özeliğini değiştirme
    I.configure(text=str(i))  #label özelliğini değişirmenin 2. yolu
    pencere.after(100,yaz)

I = Label(text="SAYAC",fg="yellow",bg="blue",font="verdana 22 bold")
I.place(x=100,y=100)
yaz()
pencere.mainloop()
