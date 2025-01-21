import tkinter as tk
from tkinter import PhotoImage
import pygame # type: ignore

pygame.mixer.init() # initialise pygame

# Fonctions
def augmenter_sucre():
    global sucre
    if sucre == 5 :
        sucre = 5
    else :
        sucre = sucre + 1
    text_id = canva.create_text(240, 300, text=f"{sucre} sucre(s)", fill="white", font=("Arial", 8))
    root.after(1000, lambda: canva.delete(text_id))

def diminuer_sucre():
    global sucre
    if sucre == 0 :
        sucre = 0
    else :
        sucre = sucre - 1
    text_id = canva.create_text(240, 300, text=f"{sucre} sucre(s)", fill="white", font=("Arial", 8))
    root.after(1000, lambda: canva.delete(text_id))

def ajouter_piece():
    global argent
    argent = round(argent + 0.50, 2)
    text_id = canva.create_text(240, 300, text=f"Solde: {argent}€", fill="white", font=("Arial", 8))
    root.after(1000, lambda: canva.delete(text_id))

def faire_espresso():
    global argent
    if argent >= 0.5 :
        argent = argent - 0.5
        text_id = canva.create_text(240, 300, text=f"Préparation..", fill="white", font=("Arial", 8))
        pygame.mixer.music.load("assets/bruit_cafe.mp3")
        pygame.mixer.music.play()
        root.after(3000, lambda: canva.itemconfig(text_id, text=f"Café prêt"))
        root.after(6000, lambda: canva.delete(text_id))
    else :
        text_id = canva.create_text(240, 300, text=f"Solde = 0€", fill="white", font=("Arial", 8))
        root.after(1000, lambda: canva.delete(text_id))

def faire_latte():
    global argent
    if argent >= 0.5 :
        argent = argent - 0.5
        text_id = canva.create_text(240, 300, text=f"Préparation..", fill="white", font=("Arial", 8))
        pygame.mixer.music.load("assets/bruit_cafe.mp3")
        pygame.mixer.music.play()
        root.after(3000, lambda: canva.itemconfig(text_id, text=f"Café prêt"))
        root.after(6000, lambda: canva.delete(text_id))
    else :
        text_id = canva.create_text(240, 300, text=f"Solde = 0€", fill="white", font=("Arial", 8))
        root.after(3000, lambda: canva.delete(text_id))

def faire_allonge():
    global argent
    if argent >= 0.5 :
        argent = argent - 0.5
        text_id = canva.create_text(240, 300, text=f"Préparation..", fill="white", font=("Arial", 8))
        pygame.mixer.music.load("assets/bruit_cafe.mp3")
        pygame.mixer.music.play()
        root.after(3000, lambda: canva.itemconfig(text_id, text=f"Café prêt"))
        root.after(6000, lambda: canva.delete(text_id))
    else :
        text_id = canva.create_text(240, 300, text=f"Solde = 0€", fill="white", font=("Arial", 8))
        root.after(3000, lambda: canva.delete(text_id))


# Variables
sucre = 3
argent = 0


# Fenetre tkinter
root = tk.Tk()
root.title("kaffee")
canva = tk.Canvas(root, width=300, height=600)
canva.grid(columnspan=30, rowspan=60)
background_image = PhotoImage(file="assets/machine_cafe_V4.png")
canva.create_image(0, 0, anchor="nw", image=background_image)


# Boutons de la machine à café
moins_sucre = tk.Button(root, text="-", command=diminuer_sucre)
moins_sucre.place(x=40, y=290, anchor="n")

text_sucre = tk.Label(root, text="SUCRE")
text_sucre.place(x=70, y=290, anchor="n")

plus_sucre = tk.Button(root, text="+", command=augmenter_sucre)
plus_sucre.place(x=105, y=290, anchor="n")

espresso = tk.Button(root, text="Espresso", font=("Arial", 8), command=faire_espresso)
espresso.place(x=55, y=335, anchor="n")

latte = tk.Button(root, text="Latte", font=("Arial", 8), command=faire_latte)
latte.place(x=105, y=335, anchor="n")

allonge = tk.Button(root, text="Allongé", font=("Arial", 8), command=faire_allonge)
allonge.place(x=150, y=335, anchor="n")

payer_carte = tk.Button(root, text="Pay", bg="white", bd=0, command=ajouter_piece)
payer_carte.place(x=242, y=340, anchor="n")

root.mainloop()