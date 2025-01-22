import tkinter as tk
from tkinter import PhotoImage
import pygame # type: ignore
pygame.mixer.init()

class kaffeeautomat():
    #Fonction initiale
    def __init__(self):
        #Variables
        self.sucre = 3
        self.argent = 0
        self.nb_espresso = 10
        self.nb_latte = 10
        self.nb_allonge = 10

        #Fenêtre
        self.root = tk.Tk()
        self.root.title("kaffee")
        self.canva = tk.Canvas(self.root, width=300, height=600)
        self.canva.grid(columnspan=30, rowspan=60)
        self.background_image = PhotoImage(file="assets/machine_cafe_V4.png")
        self.canva.create_image(0, 0, anchor="nw", image=self.background_image)

        #Boutons et Labels
        moins_sucre = tk.Button(self.root, text="-", command=self.diminuer_sucre)
        moins_sucre.place(x=40, y=290, anchor="n")

        text_sucre = tk.Label(self.root, text="SUCRE")
        text_sucre.place(x=70, y=290, anchor="n")

        plus_sucre = tk.Button(self.root, text="+", command=self.augmenter_sucre)
        plus_sucre.place(x=105, y=290, anchor="n")

        espresso = tk.Button(self.root, text="Espresso", font=("Arial", 8), command=self.faire_espresso)
        espresso.place(x=55, y=335, anchor="n")

        latte = tk.Button(self.root, text="Latte", font=("Arial", 8), command=self.faire_latte)
        latte.place(x=105, y=335, anchor="n")

        allonge = tk.Button(self.root, text="Allongé", font=("Arial", 8), command=self.faire_allonge)
        allonge.place(x=150, y=335, anchor="n")

        payer_carte = tk.Button(self.root, text="Pay", bg="white", bd=0, command=self.ajouter_piece)
        payer_carte.place(x=242, y=340, anchor="n")

        self.root.mainloop()

    #Fonctions liées aux boutons
    def augmenter_sucre(self):
        if self.sucre == 5 :
            self.sucre = 5
        else :
            self.sucre += 1
        text_id = self.canva.create_text(240, 300, text=f"{self.sucre} sucre(s)", fill="white", font=("Arial", 8))
        self.root.after(1000, lambda: self.canva.delete(text_id))

    def diminuer_sucre(self):
        self.sucre
        if self.sucre == 0 :
            self.sucre = 0
        else :
            self.sucre -= 1
        text_id = self.canva.create_text(240, 300, text=f"{self.sucre} sucre(s)", fill="white", font=("Arial", 8))
        self.root.after(1000, lambda: self.canva.delete(text_id))

    def ajouter_piece(self):
        self.argent
        self.argent = round(self.argent + 0.50, 2)
        text_id = self.canva.create_text(240, 300, text=f"Solde: {self.argent}€", fill="white", font=("Arial", 8))
        self.root.after(1000, lambda: self.canva.delete(text_id))

    def fabrication(self):
        self.argent
        if self.argent >= 0.5 :
            self.argent -= 0.5
            text_id = self.canva.create_text(240, 300, text=f"Préparation..", fill="white", font=("Arial", 8))
            pygame.mixer.music.load("assets/bruit_cafe.mp3")
            pygame.mixer.music.play()
            self.root.after(3000, lambda: self.canva.itemconfig(text_id, text=f"Café prêt"))
            self.root.after(6000, lambda: self.canva.delete(text_id))
        else :
            text_id = self.canva.create_text(240, 300, text=f"Solde = 0€", fill="white", font=("Arial", 8))
            self.root.after(3000, lambda: self.canva.delete(text_id))
    
    def faire_espresso(self):
        self.fabrication()
        self.nb_espresso -= 1

    def faire_latte(self):
        self.fabrication()
        self.nb_latte -= 1

    def faire_allonge(self):
        self.fabrication()
        self.nb_allonge -= 1

machine = kaffeeautomat()