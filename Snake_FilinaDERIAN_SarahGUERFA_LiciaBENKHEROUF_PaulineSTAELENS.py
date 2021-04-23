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

COLOR_QUADR = "black"
COLOR_MUR = "black"
COLOR_MUR_BORD = "green"
COLOR_POMME = "red"
COLOR_TETE_SNAKE = "SpringGreen4"
COLOR_SNAKE = "SpringGreen2"

#######################################
# Variables globales

snake = []
tete_snack = 0
corp_snack = 0
pomme = 0

#######################################
# Fonctions

def quadrillage():
    """Dessine un quadrillage formé de carrés de côté COTE (fonction pour nous aider a bien visualise le deplacement de la pomme et du serpent)"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COLOR_QUADR)
        y += COTE
    x = 0
    while x <= LARGEUR:
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COLOR_QUADR)
        x += COTE

def ini_mur() :
    """Créer des carré noir de dimention COTE pour créer le mur (fonction provisoir, a modifier)"""
    global LIGNE, COLONE
    x0, y0, x1, y1 = 0, 0, COTE, COTE
    for i in range(LIGNE) :
        for j in range(COLONE) :
            if i == 0 or i == LIGNE-1 :
                canvas.create_rectangle((x0, y0), (x1, y1), fill=COLOR_MUR, outline=COLOR_MUR_BORD)
            elif j == 0 or j == COLONE-1 :
                canvas.create_rectangle((x0, y0), (x1, y1), fill=COLOR_MUR, outline=COLOR_MUR_BORD)
            y0 += COTE
            y1 += COTE
        y0, y1 = 0, COTE
        x0 += COTE
        x1 += COTE

def position_depart() :
    """Initialise les posistion de départ du serpent et de la pomme"""
    global COTE, LARGEUR, HAUTEUR, pomme, tete_snack, corp_snack, snake
    milieu = (LARGEUR//COTE)//2
    pomme = canvas.create_oval((COTE*milieu, COTE*milieu), (COTE*(milieu+1), COTE*(milieu+1)), fill=COLOR_POMME, outline=COLOR_POMME)
    tete_snack = canvas.create_oval((LARGEUR-(5*COTE), HAUTEUR-(3*COTE)), (LARGEUR-(4*COTE), HAUTEUR-(2*COTE)), fill=COLOR_TETE_SNAKE, outline=COLOR_TETE_SNAKE)
    snake.append(tete_snack)
    corp_snack = canvas.create_oval((LARGEUR-(4*COTE), HAUTEUR-(3*COTE)), (LARGEUR-(3*COTE), HAUTEUR-(2*COTE)), fill=COLOR_SNAKE, outline=COLOR_SNAKE)
    snake.append(corp_snack)
    corp_snack = canvas.create_oval((LARGEUR-(3*COTE), HAUTEUR-(3*COTE)), (LARGEUR-(2*COTE), HAUTEUR-(2*COTE)), fill=COLOR_SNAKE, outline=COLOR_SNAKE)
    snake.append(corp_snack)

#######################################
# Programme principale

racine = tk.Tk()
racine.title("Snake")

# Création des widgets

canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="green")

quadrillage()
ini_mur()
position_depart()

# Placement des widgets

canvas.grid()

# Événements


racine.mainloop()