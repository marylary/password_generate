from tkinter import *
import webbrowser
from password import generation
# acceder à la chaine youtube de graven
def open_graven_chanel():
    webbrowser.open_new("https://www.youtube.com/c/Gravenilvectuto")
    
# creer fenetre
window = Tk()

# personnaliser ma fenetre
window.title("Mon Application")
window.geometry("1000x500")
window.minsize(450 , 190)
window.iconbitmap(r"C:\Users\Malaury\Pictures\Camera Roll\logo.ico")
window.config(bg="#ffac33")
# les relief: FLAT, RIDGE, GROOVE, SUNKEN
boite = Frame(window, bg="#ffac33")

# ajouter texte on peut utiliser side pour positionner le texte à gauche , à droite..... expand centre le texte
label_texte = Label(boite, text="Bienvenue sur mon Application", font=("Courrier", 40), bg="#ffac33", fg="white")
label_texte.pack()

label_soustexte = Label(boite, text="Hey salut a tous c'est malaury", font=("Courrier", 25), bg="#ffac33", fg="white")
label_soustexte.pack()
boite.pack(expand=YES)

# ajouter un bouton
pointe = Button(boite, text="Acceder a ma chaine d'apprendissage", font=("Courrier", 25), bg="white", fg="#ffac33",  command= lambda: generation(window))
pointe.pack(pady=25, fill=X)

# afficher
window.mainloop()