from tkinter import *
global szo, hibaSzam, talaltBetuk
talaltBetuk=''

def hibakezeles(szo):
    jo = 0
    try:
        print(int(szo))
        szoveg["text"] = "Adjon meg egy SZÓT!, maximum 10 betű lehet"
        entryBox.delete(0, END)
    except:
        if ' ' in szo:
            szoveg["text"] = "Nem szerepelhet space a szóban"
            entryBox.delete(0, END)
        elif len(szo)>0 and len(szo)<11:
            szoHossz = len(szo)
            jo = 1
            return jo
        elif len(szo) == 0:
            szoveg["text"] = "Adjon meg egy SZÓT!, maximum 10 betű lehet"
            entryBox.delete(0, END)
        else:
            szoveg["text"] = "Adjon meg egy szót, MAXIMUM 10 betű lehet"
            entryBox.delete(0, END)

def ujrakezdes():
    global hibaSzam,talaltBetuk
    talaltBetuk=''
    button1["text"]="Küldés"
    button1.place(x=140, y=370, width=50, height=45)
    button1["command"]=lambda: kuldesGomb()
    c.delete("all")
    entryBox.place(x=70, y=320, width=200, height=37)
    szoveg["text"]="Adjon meg egy szót, maximum 10 betű lehet"
    hibaSzam=0

def vege():
    button1["command"] = lambda: ujrakezdes()
    button1["text"]="Újrakezdés"
    talaltSzo.place_forget()
    button1.place(x=130, y=370, width=70, height=45)
    szoveg["text"]="Vesztettél.., a szó: '"+szo+"' volt."
    szoveg.place(x=20, y=300, width=300, height=20)
    entryBox.place_forget()

def rajzol(hibaSzam):
    if hibaSzam == 1:
        c.create_line(30, 200, 200, 200)
    elif hibaSzam == 2:
        c.create_line(180, 200, 180, 0)
        c.create_line(170, 200, 170, 0)
    elif hibaSzam == 3:
        c.create_line(145, 200, 170, 160)
    elif hibaSzam == 4:
        c.create_line(170, 20, 50, 20)
    elif hibaSzam == 5:
        c.create_line(170, 50, 145, 20)
    elif hibaSzam == 6:
        c.create_line(100, 80, 100, 20)
    elif hibaSzam == 7:
        c.create_oval(80, 80, 115, 115)
    elif hibaSzam == 8:
        c.create_line(98, 170, 98, 115)
    elif hibaSzam == 9:
        c.create_line(98, 140, 120, 115)
    elif hibaSzam == 10:
        c.create_line(98, 140, 77, 115)
    elif hibaSzam == 11:
        c.create_line(98, 170, 77, 190)
    elif hibaSzam == 12:
        c.create_line(98, 170, 120, 190)
        entryBox.delete(0, END)
        vege()

def nyertes():
    button1["command"] = lambda: ujrakezdes()
    button1["text"] = "Újrakezdés"
    button1.place(x=130, y=370, width=70, height=45)
    talaltSzo.place_forget()
    szoveg["text"] = "Gratulálok nyertél, a szó: '" + szo + "' volt."
    szoveg.place(x=20, y=300, width=300, height=20)
    entryBox.place_forget()

def talaltBetu(tippeltbetu):
    global szo,talaltBetuk
    helyestippek = 0
    vonalak = '-' * len(szo)
    for i in range(len(szo)):
        if szo[i] in talaltBetuk:
            vonalak = vonalak[:i] + szo[i] + vonalak[i + 1:]
            helyestippek=helyestippek+1
        for letter in vonalak:
            print(letter, end='_')
            talaltSzo["text"]=vonalak
            talaltSzo.place(x=20, y=300, width=150, height=20)
        print()
    if helyestippek == len(vonalak):
        nyertes()

def probaGomb(betu,szo):
    global hibaSzam, talaltBetuk
    if len(betu)==1:
        if szo.find(betu) != -1:
            talaltBetuk = talaltBetuk+betu
            talaltBetu(betu)
            entryBox.delete(0, END)
        else:
            szoveg.place(x=110, y=300, width=300, height=20)
            szoveg["text"] = "Nincsen a szóban "+betu+" betű"
            hibaSzam=hibaSzam+1
            rajzol(hibaSzam)
            entryBox.delete(0, END)
    else:
        szoveg["text"] = "Tippeljen EGY betűt"
        entryBox.delete(0, END)

def kuldesGomb():
    global szo
    szo = entryBox.get().lower()
    if hibakezeles(szo) == 1:
        entryBox.delete(0,END)
        entryBox.place(x=270, y=320, width=20, height=37)
        szoveg["text"]="Tippeljen egy betűt"
        szoveg.place(x=130, y=300, width=300, height=20)
        button1["text"]="Próba"
        button1.place(x=255, y=370, width=50, height=30)
        button1["command"] = lambda: probaGomb(entryBox.get(),szo)
        talaltSzo["text"] = '-' * len(szo)
        talaltSzo.place(x=20, y=300, width=150, height=20)

if __name__ == '__main__':
    global hibaSzam
    hibaSzam = 0
    ablak = Tk()
    ablak.configure(background="#FFFFFF")
    ablak.title("Akasztófa")
    ablak.geometry("350x435")

    c = Canvas(ablak, width=200, height=250)
    c.pack()
    beker = StringVar()
    entryBox = Entry(ablak, textvariable=beker, border="2", font=("Arial", 20))
    entryBox.place(x=70, y=320, width=200, height=37)

    szoveg = Label(ablak, text='Adjon meg egy szót, maximum 10 betű lehet', bg='white', fg='black', font=("Arial", 10))
    szoveg.place(x=20, y=300, width=300, height=20)

    talaltSzo = Label(ablak, text='', bg='white', fg='black', font=("Arial", 15))
    talaltSzo.place(x=20, y=300, width=17, height=20)
    talaltSzo.place_forget()

    button1 = Button(ablak, text='Küldés', fg='black', bg='white', command=lambda: kuldesGomb())
    button1.place(x=140, y=370, width=50, height=45)

    ablak.mainloop()
