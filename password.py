from cProfile import label
import imp
from random import randint
from secrets import choice
import string
from random import randint, choice
from tkinter import *
from turtle import width

def generation(fenetre):
        
    # générer mote de passe
    def generate_password():
        password_min = 6
        password_max = 12
        alls_chars = string.ascii_letters + string.punctuation + string.digits
        password = "".join(choice(alls_chars) for x in range(randint(password_min, password_max)))
        password_input.delete(0,END)
        password_input.insert(0, password)
        
        
    # creer fenetre
    fen = Toplevel(fenetre)
    fen.title("Generateur de mot de passe")
    fen.geometry("780x420")
    fen.iconbitmap(r"C:\Users\Malaury\Pictures\Camera Roll\logo.ico")
    fen.config(bg="#9ea98a")

    # creer une boite
    frame = Frame(fen, bg="#9ea98a")

    # sous boite à droite dans la boite principale
    right_frame = Frame(frame, bg="#9ea98a")

    # creer image
    lageur = 300
    hauteur = 300
    # highlightthickness > la taiile de la bordure a 0
    image = PhotoImage(file="C:\\Users\\Malaury\\Desktop\\mon_projet_python\\fistprojet\\pass.gif")
    canvas = Canvas(frame, width=lageur, height=hauteur, bg="#9ea98a", bd=0, highlightthickness=0)
    canvas.create_image(lageur/2, hauteur/2, image = image)

    # positionnement
    canvas.grid(row=0, column=0, sticky=W)
    right_frame.grid(row=0, column=1, sticky=W)
    label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg="#9ea98a", fg="#000000")
    label_title.pack()

    # input
    password_input = Entry(right_frame, font=("Helvetica", 20), bg="#9ea98a", fg="#000000")
    password_input.pack()

    #bouton
    generate_button = Button(right_frame, text="Générer", font=("Helvetica", 20), bg="#0fa49c", fg="white", command=generate_password)
    generate_button.pack(fill=X)

    # afficher la boite principale (au centre)
    frame.pack(expand=YES)

    #creation d'une barre de menu
    menu_barre = Menu(fen)
    file_menu = Menu(menu_barre, tearoff=0)
    file_menu.add_command(label="Nouveau", command=generate_password)
    file_menu.add_command(label="Quitter", command=fen.quit)
    menu_barre.add_cascade(label="Ficher", menu=file_menu)

    # Ajouter notre menu à la fenetre
    fen.config(menu=menu_barre)

    # Afficher
    fen.mainloop()