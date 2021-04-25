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

tableau_snake = [[0] * COLONE for i in range(LIGNE)]

snake = []
tete_snake = 0
corp_snake = 0
direction = ["droite", +COTE, 0]

pomme = 0

ID_after = 0

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
    global COTE, LARGEUR, HAUTEUR, pomme, tete_snake, corp_snake, snake, tableau_snake
    milieu = (LARGEUR//COTE)//2
    pomme = canvas.create_oval((COTE*milieu, COTE*milieu), (COTE*(milieu+1), COTE*(milieu+1)), fill=COLOR_POMME, outline=COLOR_POMME)
    tete_snake = canvas.create_oval((4*COTE, 2*COTE), (5*COTE, 3*COTE), fill=COLOR_TETE_SNAKE, outline=COLOR_TETE_SNAKE)
    snake.append(tete_snake)
    tableau_snake[2][4] = 1
    corp_snake = canvas.create_oval((3*COTE, 2*COTE), (4*COTE, 3*COTE), fill=COLOR_SNAKE, outline=COLOR_SNAKE)
    snake.append(corp_snake)
    tableau_snake[2][3] = 1
    corp_snake = canvas.create_oval((2*COTE, 2*COTE), (3*COTE, 3*COTE), fill=COLOR_SNAKE, outline=COLOR_SNAKE)
    snake.append(corp_snake)
    tableau_snake[2][2] = 1

def move_snake(event=0) :
    """Fonction qui deplace le serpent dans une direction (près choisie dans d'autres fonction : move_haut/bas/gauche/bas) en prennant la queue du serpent pour qu'elle devienner sa nouvelle tête"""
    global snake, direction, corp_snake, tableau_snake, COTE, ID_after
    corp_snake = snake[-1]
    tete_snake = snake[0]
    # Gére la position du serpent dans le tableau_snake avant deplacement
    x = int(canvas.coords(corp_snake)[0] // COTE)
    y = int(canvas.coords(corp_snake)[1] // COTE)
    tableau_snake[y][x] = 0
    # Gére deplacement du serpent sur le canvas 
    canvas.coords(corp_snake, canvas.coords(tete_snake)[0] + direction[1], canvas.coords(tete_snake)[1] + direction[2], canvas.coords(tete_snake)[2]+ direction[1], canvas.coords(tete_snake)[3] + direction[2])
    canvas.itemconfigure(snake[-1], fill=COLOR_TETE_SNAKE, outline=COLOR_TETE_SNAKE)
    canvas.itemconfigure(snake[0], fill=COLOR_SNAKE, outline=COLOR_SNAKE)
    snake.insert(0, snake[-1])
    del snake[-1]
    # Gére la position du serpent dans le tableau_snake aprés deplacement
    x = int(canvas.coords(corp_snake)[0] // COTE)
    y = int(canvas.coords(corp_snake)[1] // COTE)
    tableau_snake[y][x] = 1
    ID_after = racine.after(300, move_snake, event)

def move_haut(event) :
    """Fonction qui premet choisir la direction haut qui est relié a la touche z du clavier"""
    global direction
    if direction[0] != "bas" :
        direction[0] = "haut"
        direction[1] = 0
        direction[2] = -COTE

def move_bas(event) :
    """Fonction qui premet choisir la direction bas qui est relié a la touche s du clavier"""
    global direction
    if direction[0] != "haut" :
        direction[0] = "bas"
        direction[1] = 0
        direction[2] = +COTE

def move_gauche(event) :
    """Fonction qui premet choisir la direction gauche qui est relié a la touche q du clavier"""
    global direction
    if direction[0] != "droite" :
        direction[0] = "gauche"
        direction[1] = -COTE
        direction[2] = 0

def move_droite(event) :
    """Fonction qui premet choisir la direction droite qui est relié a la touche d du clavier"""
    global direction
    if direction[0] != "gauche" :
        direction[0] = "droite"
        direction[1] = +COTE
        direction[2] = 0

#######################################
# Programme principale

racine = tk.Tk()
racine.title("Snake")

# Création des widgets

canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="green")

quadrillage()
ini_mur()
position_depart()
move_snake()

# Placement des widgets

canvas.grid()

# Événements

racine.bind("<KeyRelease-z>", move_haut)
racine.bind("<KeyRelease-s>", move_bas)
racine.bind("<KeyRelease-q>", move_gauche)
racine.bind("<KeyRelease-d>", move_droite)

racine.mainloop()