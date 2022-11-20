from tkinter import *
vegeredmeny = ""

def gombnyom(szam):
    global vegeredmeny
    vegeredmeny = vegeredmeny + str(szam)
    szoveg.set(vegeredmeny)

def egyenlogomb():
    try:
        global vegeredmeny
        vegso = str(eval(vegeredmeny))
        szoveg.set(vegso)
        vegeredmeny = ""

    except:
        szoveg.set("ERROR")
        vegeredmeny = ""

def torles():
    global vegeredmeny
    vegeredmeny = ""
    szoveg.set("")

if __name__ == "__main__":
    felulet = Tk()

    felulet.configure(background="#ff0006")
    felulet.title("Számológép")
    felulet.geometry("300x350")

    szoveg = StringVar()
    vegeredmeny_doboz = Entry(felulet, textvariable=szoveg, font=("Arial", 16))
    vegeredmeny_doboz.grid(columnspan=4, ipadx=60)
    vegeredmeny_doboz.place(x=30,y=10, width=224, height=37)

    #GOMBOK
    button1 = Button(felulet, text=' 1 ', fg='black', bg='white', command=lambda: gombnyom(1), height=1, width=5, font=("Arial", 20), borderwidth=3, relief="groove")
    button1.grid(row=2, column=0)
    button1.place(x=10,y=60, width=50, height=45)

    button2 = Button(felulet, text=' 2 ', fg='black', bg='white', command=lambda: gombnyom(2), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    button2.grid(row=2, column=1)
    button2.place(x=70, y=60, width=50, height=45)

    button3 = Button(felulet, text=' 3 ', fg='black', bg='white', command=lambda: gombnyom(3), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    button3.grid(row=2, column=2)
    button3.place(x=130, y=60, width=50, height=45)

    button4 = Button(felulet, text=' 4 ', fg='black', bg='white', command=lambda: gombnyom(4), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    button4.grid(row=3, column=0)
    button4.place(x=10, y=110, width=50, height=45)

    button5 = Button(felulet, text=' 5 ', fg='black', bg='white', command=lambda: gombnyom(5), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    button5.grid(row=3, column=1)
    button5.place(x=70, y=110, width=50, height=45)

    button6 = Button(felulet, text=' 6 ', fg='black', bg='white', command=lambda: gombnyom(6), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    button6.grid(row=3, column=2)
    button6.place(x=130, y=110, width=50, height=45)

    button7 = Button(felulet, text=' 7 ', fg='black', bg='white', command=lambda: gombnyom(7), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    button7.grid(row=4, column=0)
    button7.place(x=10, y=160, width=50, height=45)

    button8 = Button(felulet, text=' 8 ', fg='black', bg='white', command=lambda: gombnyom(8), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    button8.grid(row=4, column=1)
    button8.place(x=70, y=160, width=50, height=45)

    button9 = Button(felulet, text=' 9 ', fg='black', bg='white', command=lambda: gombnyom(9), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    button9.grid(row=4, column=2)
    button9.place(x=130, y=160, width=50, height=45)

    button0 = Button(felulet, text=' 0 ', fg='black', bg='white', command=lambda: gombnyom(0), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    button0.grid(row=5, column=0)
    button0.place(x=10, y=210, width=110, height=45)

    osszead = Button(felulet, text=' + ', fg='black', bg='white', command=lambda: gombnyom("+"), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    osszead.grid(row=2, column=3)
    osszead.place(x=220, y=60, width=72, height=45)

    minusz = Button(felulet, text=' - ', fg='black', bg='white', command=lambda: gombnyom("-"), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    minusz.grid(row=3, column=3)
    minusz.place(x=220, y=110, width=72, height=45)

    szorzas = Button(felulet, text=' * ', fg='black', bg='white', command=lambda: gombnyom("*"), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    szorzas.grid(row=4, column=3)
    szorzas.place(x=220, y=160, width=72, height=45)

    osztas = Button(felulet, text=' / ', fg='black', bg='white', command=lambda: gombnyom("/"), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    osztas.grid(row=5, column=3)
    osztas.place(x=220, y=210, width=72, height=45)

    egyenlo = Button(felulet, text=' = ', fg='black', bg='white', command=egyenlogomb, height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    egyenlo.grid(row=5, column=2)
    egyenlo.place(x=190, y=290, width=100, height=45)

    torles = Button(felulet, text='Törlés', fg='black', bg='white',  command=torles, height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    torles.grid(row=5, column='1')
    torles.place(x=10, y=290, width=100, height=45)

    pont = Button(felulet, text='.', fg='black', bg='white', command=lambda: gombnyom('.'), height=1, width=7, font=("Arial", 20), borderwidth=3, relief="groove")
    pont.grid(row=6, column=0)
    pont.place(x=130, y=210, width=50, height=45)
    felulet.mainloop()