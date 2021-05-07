from tkinter import *
import os
import tkinter
import tkinter as tk
import sqlite3
from tkinter import ttk

#prozor za registraciju
def registracija():
    global registracija_prozor
    registracija_prozor = Toplevel(glavni_prozor)
    registracija_prozor.title("Registracija")
    registracija_prozor.geometry("300x150")
    registracija_prozor.resizable(width = False, height = False)

    global username
    global password
    global username_unos
    global password_unos
    username = StringVar()
    password = StringVar()

    username_label = Label(registracija_prozor, text="Korisnik")
    username_label.pack()

    username_unos = Entry(registracija_prozor, textvariable=username)
    username_unos.pack()

    password_label = Label(registracija_prozor, text= "Lozinka")
    password_label.pack()

    password_unos = Entry(registracija_prozor, textvariable=password, show="*")
    password_unos.pack()

    Label(registracija_prozor, text="").pack()
    Button(registracija_prozor, text="Registruj se", width=10, height=1, bg="blue", command = registruj).pack()
    

#prozor za prijavljivanje

def prijava():
    global prijava_prozor
    prijava_prozor = Toplevel(glavni_prozor)
    prijava_prozor.title("Prijava")
    prijava_prozor.geometry("300x150")
    prijava_prozor.resizable(width = False, height = False)

    global username_potvrda
    global password_potvrda

    username_potvrda = StringVar()
    password_potvrda = StringVar()

    global username_prijava_unos
    global password_prijava_unos

    Label(prijava_prozor, text="Korisnik").pack()
    username_prijava_unos = Entry(prijava_prozor, textvariable=username_potvrda)
    username_prijava_unos.pack()

    Label(prijava_prozor, text="Lozinka").pack()
    password_prijava_unos = Entry(prijava_prozor, textvariable=password_potvrda, show="*")
    password_prijava_unos.pack()

    Label(prijava_prozor, text="").pack()
    Button(prijava_prozor, text="Prijavi se", width=10, height=1, bg="blue", command = prijavi_se).pack()

#registraciono dugme

def registruj():
    
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(username_info)
    file.close()

    username_unos.delete(0, END)
    password_unos.delete(0, END)

    Label(registracija_prozor, text="Uspesno ste se registrovali!", fg="green", font=("calibri", 11)).pack()

# prijava dugme

def prijavi_se():
    
    username1 = username_potvrda.get()
    password1 = password_potvrda.get()
    username_prijava_unos.delete(0, END)
    password_prijava_unos.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            apoteka()
        else:
            password_greska()


    else:
        username_greska()
# prozor koji se otvara prilikom pretrage
def pretraga_prozor1():
    global pretraga_prozor
    pretraga_prozor= Tk()
    pretraga_prozor = Toplevel(root)
    pretraga_prozor.title("Prikaz pretrage")
    pretraga_prozor.geometry("1200x600")
    pretraga_prozor.configure(bg = 'green')
    pretraga_prozor.resizable(width = False, height = False)

    w = Label(pretraga_prozor, text = "Prikaz pretrage",bg = "green") 
    w.config(font =("Courier", 15))
    w.pack()

    Korpa = Button(pretraga_prozor, text = "Dodaj u korpu", padx = 50, pady =10, bg ='yellow', cursor = 'hand2')
    Korpa.place(x = 975,y =550)

# prozor za korpu
def korpa_prozor1():
    global korpa_prozor
    korpa_prozor= Tk()
    korpa_prozor = Toplevel(root)
    korpa_prozor.title("Prikaz korpe")
    korpa_prozor.geometry("300x600")
    korpa_prozor.configure(bg = 'green')
    korpa_prozor.resizable(width = False, height = False)

    w = Label(korpa_prozor, text = "Vasa korpa",bg = "green") 
    w.config(font =("Courier", 15))
    w.pack()

    racun = Button(korpa_prozor, text = "Racun", padx = 50, pady =10, bg ='red', cursor = 'hand2')
    racun.place(x = 80,y =550)
    
#prozor za kontakt

def kontakt_prozor1():
    global kontakt_prozor
    kontakt_prozor= Tk()
    kontakt_prozor = Toplevel(root)
    kontakt_prozor.title("PKontakt informacije")
    kontakt_prozor.geometry("500x500")
    kontakt_prozor.configure(bg = 'green')
    kontakt_prozor.resizable(width = False, height = False)

    w = Label(kontakt_prozor, text = "Informacije",bg = "green") 
    w.config(font =("Courier", 15))
    w.pack()

    bogdan = Label(kontakt_prozor, text = "ime: Bogdan Tomic")
    bogdan.config(font =("Courier", 10))
    bogdan.pack()
    bogdan_index = Label(kontakt_prozor, text = "index: i001-14/2019")
    bogdan_index.config(font =("Courier", 10))
    bogdan_index.pack()
    bogdan_gmail = Label(kontakt_prozor, text = "gmail: boki.tomic001@gmail.com")
    bogdan_gmail.config(font =("Courier", 10))
    bogdan_gmail.pack()
    

    bosko = Label(kontakt_prozor, text = "ime: Bosko Paunovic")
    bosko.config(font =("Courier", 10))
    bosko.pack()
    bosko_index = Label(kontakt_prozor, text = "index: i001-55/2019")
    bosko_index.config(font =("Courier", 10))
    bosko_index.pack()
    bosko_gmail = Label(kontakt_prozor, text = "gmail: bosko29195@gmail.com")
    bosko_gmail.config(font =("Courier", 10))
    bosko_gmail.pack()

    

# prozor apoteke
def apoteka():

    global root
    root = Toplevel(prijava_prozor)
    #inicijalizacija prozora
    root = Tk()
    root.geometry("1200x600")
    root.resizable(width = False, height = False)
    root.configure(bg = 'green')
  
    #Naslov
    l = Label(root, text = "Apoteka",bg = "green") 
    l.config(font =("Courier", 30))
    l.pack()


    #naziv prozora
    root.wm_title("Apoteka")

    #pretraga
    Pretraga = Entry(root, width = 100, textvariable=1)
    Pretraga.pack(ipady=3)
    #dugme pretraga
    Trazi_pretraga = Button(root, text = "Trazi", padx = 54, pady =7, bg='blue', command=pretraga_prozor1)
    Trazi_pretraga.place(x = 858,y =100)
    Trazi_pretraga.pack()

    #kontakt dugme
    Kontakt = Button(root, text = "Kontakt", padx = 80, pady =6, bg = 'red', cursor = 'hand2', command=kontakt_prozor1)
    Kontakt.place(x = 975,y =550)

    #korpa dugme
    Korpa = Button(root, text = "Korpa", padx = 40, pady =10, bg ='yellow', cursor = 'hand2', command=korpa_prozor1)
    Korpa.place(x = 1065,y =8)

    #sa receptom dugme
    SaReceptom= Button(root, text = "Izdavanje na recept", padx = 20, pady = 5)
    SaReceptom.config(font=("Courier",20))
    SaReceptom.place(x = 228, y = 160)
    #bez recepta dugme
    BezRecepta= Button(root, text = "Izdavanje bez recepta", padx = 20, pady = 5)
    BezRecepta.config(font=("Courier",20))
    BezRecepta.place(x = 600, y = 160)

    #proizvodjaci
    proizvodjaci = ["Bayer", "Hemofarm","Galenika"] #izvuci ovo iz db
    var = tk.StringVar(root)
    var.set("Proizvodjaci")
    opt = tk.OptionMenu(root,var, *proizvodjaci)
    opt.config(width = 15,height = 1, font=("Courier",20))
    opt.place(x = 227, y = 245)

    Trazi2 = Button(root, text = "Trazi", padx = 23, pady =11,bg = 'blue')
    Trazi2.place(x = 514,y =246)

    #Kategorija
    kategorija = ["Analgetik", "Antibiotik", "Antipiretik"] #izvuci iz db
    varr = tk.StringVar(root)
    varr.set("Kategorija")
    opt2 = tk.OptionMenu(root,varr, *kategorija)
    opt2.config(width = 15,height = 1, font=("Courier",20))
    opt2.place(x = 600, y = 245)

    Trazi3 = Button(root, text = "Trazi", padx = 23, pady =11,bg = 'blue')
    Trazi3.place(x = 890,y =246)

    #prikaz prozora
    root.mainloop()

#sifra greska

def password_greska():
    global password_greska_prozor
    password_greska_prozor = Toplevel(prijava_prozor)
    password_greska_prozor.title("Greska")
    password_greska_prozor.geometry("150x100")
    password_greska_prozor.resizable(width = False, height = False)
    Label(password_greska_prozor, text="Pogresna lozinka").pack()
    Button(password_greska_prozor, text ="OK", command= obrisi_password_greska).pack()

# korisnik greska

def username_greska():
    global username_greska_prozor
    username_greska_prozor = Toplevel(prijava_prozor)
    username_greska_prozor.title("Greska")
    username_greska_prozor.geometry("150x100")
    username_greska_prozor.resizable(width = False, height = False)
    Label(username_greska_prozor, text="Korisnik nije pronadjen").pack()
    Button(username_greska_prozor, text ="OK", command= obrisi_username_greska).pack()

#brisanje prozora

def obrisi_password_greska():
    password_greska_prozor.destroy()

def obrisi_username_greska():
    username_greska_prozor.destroy()


#pocetni prozor

def glavni_prozor():
    global glavni_prozor
    glavni_prozor = Tk()
    glavni_prozor.geometry("300x200")
    glavni_prozor.title("Izbor korisnika")
    glavni_prozor.resizable(width = False, height = False)
    Label(text="Sta zelite da uradite?", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Prijava", height="2", width="30", command = prijava).pack()
    Label(text="").pack()
    Button(text="Registrujte se ", height="2", width="30", command=registracija).pack()
 
    glavni_prozor.mainloop()

glavni_prozor()
    
