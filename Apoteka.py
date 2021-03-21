import tkinter
from tkinter import *
import tkinter as tk
import sqlite3


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
Pretraga = Text(root, bg = 'white', fg='black', bd=0, width=35, height=1, relief=SUNKEN, cursor='hand2')
Pretraga.config(font = ("Courier", 25))
Pretraga.insert(INSERT, "Pretraga po nazivu")
Pretraga.place(x=230,y=100)
#dugme pretraga
Trazi = Button(root, text = "Trazi", padx = 54, pady =7, bg='blue')
Trazi.place(x = 858,y =100)

#kontakt dugme
Kontakt = Button(root, text = "Kontakt", padx = 80, pady =6, bg = 'red', cursor = 'hand2')
Kontakt.place(x = 975,y =550)

#korpa dugme
Korpa = Button(root, text = "Korpa", padx = 40, pady =10, bg ='yellow', cursor = 'hand2')
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
proizvodjaci = ["Proizvodjaci","Bayer", "Hemofarm","Galenika"] #izvuci ovo iz db
var = tk.StringVar(root)
var.set(proizvodjaci[0])
opt = tk.OptionMenu(root,var, *proizvodjaci)
opt.config(width = 15,height = 1, font=("Courier",20))
opt.place(x = 227, y = 245)

Trazi2 = Button(root, text = "Trazi", padx = 23, pady =11,bg = 'blue')
Trazi2.place(x = 514,y =246)

#Kategorija
kategorija = ["Kategorija","Analgetik", "Antibiotik", "Antipiretik"] #izvuci iz db
varr = tk.StringVar(root)
varr.set(kategorija[0])
opt2 = tk.OptionMenu(root,varr, *kategorija)
opt2.config(width = 15,height = 1, font=("Courier",20))
opt2.place(x = 600, y = 245)

Trazi3 = Button(root, text = "Trazi", padx = 23, pady =11,bg = 'blue')
Trazi3.place(x = 890,y =246)

#prikaz prozora
root.mainloop()
