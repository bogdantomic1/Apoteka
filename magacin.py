from tkinter import *
from tkinter.ttk import Treeview
from db import Baza
from tkinter import messagebox
from functools import partial  

#Povezivanje baze 
db = Baza('lek.db')

 

#Funkcije

def popuni(naziv=''):
    for i in lek_tree_view.get_children():
        lek_tree_view.delete(i)
    for redovi in db.pokupi1(naziv):
        lek_tree_view.insert('', 'end', values=redovi)


def dodaj(x, y):
    global cena, stanje
    try:
        cena = int(x.get())
        stanje = int(y.get())
        if pr_text.get() == '' or naziv_text.get() == '' or cena_text.get() == '' or stanje_text.get() == '':
            messagebox.showerror('GRESKA!', 'Popunite sva polja!')
            return
        
        db.ubaci(naziv_text.get(), pr_text.get(), cena, stanje)
    except ValueError:
        messagebox.showerror('GRESKA!', ' Unesite broj!')
    
    obrisi()
    popuni()


def selektuj(event):
    try:
        global odabrani_lek
        index = lek_tree_view.selection()[0]
        odabrani_lek = lek_tree_view.item(index)['values']
        naziv_unos.delete(0, END)
        naziv_unos.insert(END, odabrani_lek[1])
        pr_unos.delete(0, END)
        pr_unos.insert(END, odabrani_lek[2])
        cena_unos.delete(0, END)
        cena_unos.insert(END, odabrani_lek[3])
        stanje_unos.delete(0, END)
        stanje_unos.insert(END, odabrani_lek[4])
    except IndexError:
        pass

def ukloni():
    db.izbrisi(odabrani_lek[0])
    obrisi()
    popuni()

def azuriraj(x, y):
    try:
        cena = int(x.get()) 
        stanje = int(y.get())
        db.azuriraj(odabrani_lek[0], naziv_text.get(), pr_text.get(),
              cena, stanje)
    except ValueError:
        messagebox.showerror('GRESKA!', ' Unesite broj!')

    
    popuni()

def obrisi():
    pr_unos.delete(0, END)
    naziv_unos.delete(0, END)
    cena_unos.delete(0, END)
    stanje_unos.delete(0, END)




#Inicijalizacija prozora

prozor = Tk()
sirina= prozor.winfo_screenwidth() 
visina= prozor.winfo_screenheight()

prozor.geometry("%dx%d" % (sirina, visina))
prozor.resizable(width = False, height = False)
prozor.configure(bg = 'peach puff')
prozor.title('Magacin')

#Kreiranje polja za unos podataka

okvir_polja = Frame(prozor,  bg = 'peach puff')
okvir_polja.grid(row=0, column=0, rowspan=3, padx = 70, ipady = 120)
#naziv
naziv_text = StringVar()
naziv_label = Label(okvir_polja, text='Naziv leka:', font=('bold', 18), bg = 'peach puff', pady = 30 )
naziv_label.grid(row=0, column=0, sticky=W)
naziv_unos = Entry(okvir_polja, textvariable=naziv_text, font=(20))
naziv_unos.grid(row=1, column=0, sticky=W)
#proizvodjac
pr_text = StringVar()
pr_label = Label(okvir_polja, text='Proizvodjac:', font=('bold', 18), bg = 'peach puff', pady = 30)
pr_label.grid(row=2, column=0, sticky=W)
pr_unos = Entry(okvir_polja, textvariable=pr_text, font=(20))
pr_unos.grid(row=3, column=0, sticky=W)
#cena
cena_text = StringVar()
cena_label = Label(okvir_polja, text='Cena:', font=('bold', 18), bg = 'peach puff', pady = 30)
cena_label.grid(row=4, column=0, sticky=W)
cena_unos = Entry(okvir_polja, textvariable=cena_text, font=(20))
cena_unos.grid(row=5, column=0, sticky=W)
#stanje
stanje_text = StringVar()
stanje_label = Label(okvir_polja, text='Stanje:', font=('bold', 18), bg = 'peach puff', pady=30)
stanje_label.grid(row=6, column=0, sticky=W)
stanje_unos = Entry(okvir_polja, textvariable=stanje_text, font=(20))
stanje_unos.grid(row=7, column=0, sticky=W)



#Prikaz podataka iz baze uz pomoc Tree view prikaza

okvir_podataka = Frame(prozor)
okvir_podataka.grid( row=0, column = 3 , rowspan=3, ipady=250)

columns = ['Sifra', 'Naziv', 'Proizvodjac', 'Cena', 'Stanje']
lek_tree_view = Treeview(okvir_podataka, columns=columns, show="headings")

for col in columns[0:]:
        lek_tree_view.column(col, width=200)
        lek_tree_view.heading(col, text=col)
lek_tree_view.bind('<<TreeviewSelect>>', selektuj)
lek_tree_view.pack(side="left", fill="y")
scrollbar = Scrollbar(okvir_podataka, orient='vertical')
scrollbar.configure(command=lek_tree_view.yview)
scrollbar.pack(side="right", fill="y")
lek_tree_view.config(yscrollcommand=scrollbar.set)

#Kreiranje dugmica

okvir_dugmica = Frame(prozor,  bg = 'peach puff')
okvir_dugmica.grid(row=4, column=2, columnspan = 2)
dodaj = partial(dodaj, cena_text, stanje_text)
dodaj_dugme = Button(okvir_dugmica, text='Dodaj', width=20, command=dodaj,  bg = 'cadet blue', font=(18))
dodaj_dugme.grid(row=0, column=0, pady=20)

ukloni_dugme = Button(okvir_dugmica, text='Ukloni',
                    width=20, command=ukloni, bg = 'red', font=(18))
ukloni_dugme.grid(row=0, column=1)
azuriraj = partial(azuriraj, cena_text, stanje_text)
azuriraj_dugme = Button(okvir_dugmica, text='Azuriraj',
                    width=20, command=azuriraj, bg = 'yellow', font=(18))
azuriraj_dugme.grid(row=0, column=2)

ocisti_dugme = Button(okvir_dugmica, text='Ocisti',
                   width=20, command=obrisi, bg = 'lime green', font=(18))
ocisti_dugme.grid(row=0, column=3)

#Popuni podatke
popuni()

#Pokreni program
prozor.mainloop()

