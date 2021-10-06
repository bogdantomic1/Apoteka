from tkinter import *
from tkinter.ttk import Treeview
from db import Baza
from tkinter import messagebox
from functools import partial  
from RacunDB import Racun
import random
from time import strftime


#Inicijalizacija prozora i uvodjenje baza podataka

db = Baza('lek.db')
db2 = Racun('racun.db')
prozor = Tk()
sirina= prozor.winfo_screenwidth() 
visina= prozor.winfo_screenheight()

prozor.geometry("%dx%d" % (sirina, visina))
prozor.resizable(width = False, height = False)
prozor.configure(bg = 'lime green')
prozor.title('Apoteka')
#Definisanje funkcije za sat

def sat():
    vreme = strftime('%H:%M:%S %p')
    lb = Label(prozor, bg='limegreen', font=(30))
    lb.config(text = vreme)
    lb.after(1000, sat)
    lb.grid(row = 0, column=6)
sat()

#Funkcije
def selektuj(event):
    
    try:
        global n, c, s,odabrani_lek
        n = ''
        c = 0
        index = lek_tree_view.selection()[0]
        odabrani_lek = lek_tree_view.item(index)['values']
       
        n = odabrani_lek[1]
        c = odabrani_lek[3]
        s = 1
    except IndexError:
        pass

    
def selektuj2(event):
    try:
        global odabrani_lek2
        index = racun_tree_view.selection()[0]
        odabrani_lek2 = racun_tree_view.item(index)['values']
        
    except IndexError:
        pass

def popuni(naziv=''):
    for i in lek_tree_view.get_children():
        lek_tree_view.delete(i)
    for redovi in db.pokupi1(naziv):
        lek_tree_view.insert('', 'end', values=redovi)

def pretrazuj():
    naziv = pretraga.get()
    popuni(naziv)
    
def popuni_racun(naziv=''):
    for i in racun_tree_view.get_children():
        racun_tree_view.delete(i)
    for redovi in db2.pokupi(naziv):
        racun_tree_view.insert('', 'end', values=redovi)


iznos = 0     
def iznos_racuna_plus(x):
    global iznos
    iznos += x
    iznos_lbl.configure(text='Iznos je: %d' % iznos + 'rsd')


def iznos_racuna_minus(x):
    global iznos
    iznos -= x
    if iznos <0:
        iznos = 0
    iznos_lbl.configure(text='Iznos je: %d' % iznos + 'rsd')



def dodaj_na_racun():
    odabrani_lek[4] = odabrani_lek[4] - s
    if odabrani_lek[4]<0:
        messagebox.showerror('GRESKA!', 'Ne moze bit imanje od 0')
        return
    
    db.azuriraj(odabrani_lek[0], odabrani_lek[1], odabrani_lek[2], odabrani_lek[3], odabrani_lek[4])
    db2.ubaci(n, c, s)
    iznos_racuna_plus(odabrani_lek[3])
    popuni_racun()
    

def obrisi_sa_racuna():
    vracanje_na_stanje()
    db2.izbrisi(odabrani_lek2[0])
    
    iznos_racuna_minus(odabrani_lek2[2])
    popuni_racun()


#Funkcije za racun i kasu
    
name = ""
kasa_iznos = 0
def ocisti_racun():
    racun_tree_view.delete(*racun_tree_view.get_children())
    global iznos
    iznos = 0


def racun_txt():
    lista = []
    x = random.randint(1, 100000)
    if x not in lista:
        lista.append(x)
    else:
        x = random.randint(1, 1000000)
    global name
    name = "racun%d" % (x)
    file = open("%s.txt" % (name), 'w' )
    with open("%s.txt" % (name),"w") as file:
        file.write("\t    \t   Fiskalni racun br. %d\n" % (x))

    for redovi in db2.stampaj():
        with open("%s.txt" % (name),"a") as file:
            file.write("Artikal: %s ---------- Cena: %d\n" % (redovi[1], redovi[2]))
    with open("%s.txt" % (name),"a") as file:
            file.write("\nZa uplatu: %d\n" % (iznos))
    with open("%s.txt" % (name),"a") as file:
            file.write("\n====================================\n")
    file.close()
    global kasa_iznos
    kasa_iznos += iznos
    ocisti_racun()
    db2.obrisi()


def stanje_kase():
    global kasa_iznos
    kasa_lbl.configure(text='U kasi je: %d' % kasa_iznos + ' rsd')


file = open("Zarada.txt", 'a')
with open("Zarada.txt",'w') as file:
    file.write("\t     Ukupna zarada \n")


def presek_stanja():
    global kasa_iznos
    file = open("Zarada.txt", 'a')
    with open("Zarada.txt",'a') as file:
        file.write("Zarada pri ovom preseku je: %d rsd\n" % kasa_iznos)
    with open("Zarada.txt",'a') as file:
        file.write("------------------------------------\n" )
    file.close()
    kasa_iznos= 0


    


def vracanje_na_stanje():
    x =0
    global odabrani_lek2
     #################ne radi
    for redovi2 in db.stampaj():
        if odabrani_lek2[1] == redovi2[1]:
            x = redovi2[4]+1
            db.azuriraj(redovi2[0], redovi2[1], redovi2[2], redovi2[3], x)
               
            
            
        
    

#Dugmici i polja za input
#presek
presek = Button(prozor, text = "Presek", padx = 70, pady =10, bg='yellow', command =presek_stanja)
presek.grid(row = 10, column = 0, sticky="E")
#pretraga polje za unos
pretraga = StringVar()
Pretraga = Entry(prozor, width = 145, textvariable=pretraga)
Pretraga.grid(row = 0, column = 0, columnspan = 10, pady = 5, padx = 10, sticky="W")

#dugme pretraga
Trazi_pretraga = Button(prozor, text = "Trazi/Osvezi", padx = 70, pady =10, bg='blue', command =pretrazuj)
Trazi_pretraga.grid(row = 1, column = 0)

#prikaz
prikaz_naslov = Label (text='Pretraga', font=('bold', 27), bg = 'lime green')
prikaz_naslov.grid(row = 2, column = 0)

# Prikaz lekova
okvir = Frame(prozor)
okvir.grid( row=3, column = 0 , rowspan=6, ipady=120, padx = 1, pady = 10)

columns = ['Sifra', 'Naziv', 'Proizvodjac', 'Cena', 'Stanje']
lek_tree_view = Treeview(okvir, columns=columns, show="headings")

for col in columns[0:]:
        lek_tree_view.column(col, width=160)
        lek_tree_view.heading(col, text=col)
lek_tree_view.bind('<<TreeviewSelect>>', selektuj)
lek_tree_view.pack(side="left", fill="y")
scrollbar = Scrollbar(okvir, orient='vertical')
scrollbar.configure(command=lek_tree_view.yview)
scrollbar.pack(side="right", fill="y")
lek_tree_view.config(yscrollcommand=scrollbar.set)

#Jos dugmica - za rad izmedju baza (magacin i racun)
dodaj  = Button(prozor, text = "Dodaj na racun", padx = 50, pady =10, bg='cadet blue', command = dodaj_na_racun)
dodaj.grid(row = 4, column = 3)

ukloni  = Button(prozor, text = "Vrati na stanje", padx = 50, pady =10, bg='red', command = obrisi_sa_racuna)
ukloni.grid(row = 5, column = 3)

stampaj  = Button(prozor, text = "Stampaj racun", padx = 55, pady =10, bg='orange', command=racun_txt)
stampaj.grid(row = 10, column = 6, pady = 10)

kasa  = Button(prozor, text = "Stanje kase", padx = 55, pady =10, bg='yellow', command=stanje_kase)
kasa.grid(row = 10, column = 0, pady = 120)


#Prikaz iznosa i stanja kase
iznos_lbl = Label(font=('bold', 27), bg = 'lime green')
iznos_lbl.grid(row=2, column= 6)

kasa_lbl = Label(font=('bold', 15), bg = 'lime green')
kasa_lbl.grid(row=10, column= 0, sticky="w")

#Prikaz racuna
okvir2 = Frame(prozor)
okvir2.grid( row=3, column = 6 , rowspan=6, padx = 1, pady = 1, ipady = 150)

columns2 = ['Sifra', 'Naziv', 'Cena', 'Kolicina']
racun_tree_view = Treeview(okvir2, columns=columns2, show="headings")

for col in columns2[0:]:
        racun_tree_view.column(col, width=100)
        racun_tree_view.heading(col, text=col)
racun_tree_view.bind('<<TreeviewSelect>>', selektuj2)
racun_tree_view.pack(side="left", fill="y")
scrollbar2 = Scrollbar(okvir2, orient='vertical')
scrollbar2.configure(command=racun_tree_view.yview)
scrollbar2.pack(side="right", fill="y")
racun_tree_view.config(yscrollcommand=scrollbar2.set)
#Pozivanje funkcija za baze podataka
popuni()
popuni_racun()
# Pokretanje programa
prozor.mainloop()
