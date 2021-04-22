#######################################
# groupe Bi TD-04
# BENKHEROUF Licia
# DERIAN Filina
# GUERFA Sarah
# STAELENS Pauline
# https://github.com/uvsq21921401/Projet_Snake
#######################################

#######################################
# Import des librairies

import tkinter as tk

#######################################
# Constantes (écrites en majuscule)

LARGEUR = 500
HAUTEUR = 500
COTE = 20
COLONE = LARGEUR // COTE
LIGNE = HAUTEUR // COTE

#######################################
# Variables globales

#######################################
# Fonctions

#######################################
# Programme principale

racine = tk.Tk()
racine.title("Snake")

# Création des widgets

canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="green")

# Placement des widgets

canvas.grid()

# Événements


racine.mainloop()