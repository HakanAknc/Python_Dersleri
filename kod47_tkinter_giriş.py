#GUI graphical user interface
#python'da tkinter kütüphanesi ile yapılır

import tkinter as tk
pencere = tk.Tk()
pencere.title("ilk GUI penceresi")
pencere.geometry("500x500+250+70")

#width , height, x, y

etiket = tk.Label(text="tkinter ilk componentimiz",font="Verdana 22 bold",bg="blue",fg="yellow")
etiket.pack()
etiket2 = tk.Label(text="İKİNCİ ETİKET",font="Verdana 22 bold",bg="blue",fg="yellow")
etiket2.place(x=250,y=250)

#pack8) sıra ile componentleri yerlştirir
#grid()
#place()

pencere.mainloop()
pencere2=tk.Tk()
etiket3=tk.Label(text="bende grid ile yerleştim",font="arial 22 bold")
etiket3.grid(row=0,column=0)
etiket4=tk.Label(text="grid ile yerleştim",font="arial 22 bold")
etiket4.grid(row=1,column=1)
pencere2.mainloop()
