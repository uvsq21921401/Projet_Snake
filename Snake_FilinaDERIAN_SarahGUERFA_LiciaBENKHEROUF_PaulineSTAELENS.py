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

from tkinter import*


# Programme Menu 

# Fenêtre des différents niveaux
def create1():
    easy=Tk()
    easy.geometry('800x400')
    easy.mainloop()

def create2():
    intermediate=Tk()
    intermediate.geometry('600x400')
    intermediate.mainloop()

def create3():
    difficult=Tk()
    difficult.geometry('400x400')
    difficult.mainloop()

# Fenêtre du menu
root = Tk()
root.geometry('589x400')
root.configure(bg='#88e75f')

# Bouton clic
btn = Button(root, text="Facile", command = create1,  font=("Courrier", 28), bg ="#2f6d35", fg = "#f88f7c")
btn1 = Button(root, text="Intermédiaire", command = create2,  font=("Courrier", 28), bg = "#2f6d35", fg = "#f88f7c")
btn2 = Button(root, text="Difficile", command = create3,  font=("Courrier", 28),bg = "#2f6d35", fg = "#f88f7c")


text = Label(root, text="Jeu Snake",  font=("brush script mt", 70),  bg = "#88e75f", fg = "#2f6d35")

# Coordonnées des Boutons clic
btn.place(x = 50, y = 300)
btn1.place(x = 170, y = 300)
btn2.place(x = 400, y = 300)
text.place(x = 120, y = 100)
root.mainloop()




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
COLOR_TETE_SNAKE = "Cyan3"
COLOR_SNAKE = "Green2"

#######################################
# Variables globales

"""La variable globale tableau_snake de garder en mémoire quelle case est occupé par le serpent par la valeur 1"""
tableau_snake = [[0] * COLONE for i in range(LIGNE)] 
# ===========================
# A VOIR : - on peut faire un tableau similaire pour les mur ?
# - peut nous faciliter le deplacement de la pomme, 
# exemple : si la pomme tombe sur une case avec la valeur 1 (serpent) alors elle ne peut pas aller sur cette case
# - si on fait un tableau similaire pour les mur, on pourras faire la même pour que la pomme n'apparait pas sur un mur 
# et aussi pour le serpent
# ===========================

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

def snake_grandit(x_queue, y_queue) :
    """Fonction qui ajout un rond au bout du serpent pour le faire grandir"""
    global snake, tableau_snake, corp_snake
    tableau_snake[y_queue][x_queue] = 1
    corp_snake = canvas.create_oval((x_queue*COTE, y_queue*COTE), ((x_queue+1)*COTE, (y_queue+1)*COTE), fill=COLOR_SNAKE, outline=COLOR_SNAKE)
    snake.append(corp_snake)


def move_snake(event=0) :
    """Fonction qui deplace le serpent dans une direction (près choisie dans d'autres fonction : move_haut/bas/gauche/bas) en prennant la queue du serpent pour qu'elle devienner sa nouvelle tête"""
    global snake, direction, corp_snake, tableau_snake, COTE, pomme, ID_after
    corp_snake = snake[-1]
    tete_snake = snake[0]
    # Récuper les coordonnée de la pomme
    x_pomme = canvas.coords(pomme)[0] // COTE
    y_pomme = canvas.coords(pomme)[1] // COTE
    # Gére la position de serpent dans le tableau_snake avant deplacement
    x_queue = int(canvas.coords(corp_snake)[0] // COTE)
    y_queue = int(canvas.coords(corp_snake)[1] // COTE)
    tableau_snake[y_queue][x_queue] = 0
    # Gére deplacement du serpent sur le canvas 
    canvas.coords(corp_snake, canvas.coords(tete_snake)[0] + direction[1], canvas.coords(tete_snake)[1] + direction[2], canvas.coords(tete_snake)[2]+ direction[1], canvas.coords(tete_snake)[3] + direction[2])
    canvas.itemconfigure(snake[-1], fill=COLOR_TETE_SNAKE, outline=COLOR_TETE_SNAKE)
    canvas.itemconfigure(snake[0], fill=COLOR_SNAKE, outline=COLOR_SNAKE)
    snake.insert(0, snake[-1])
    del snake[-1]
    # Gére la position de serpent dans le tableau_snake aprés deplacement et gestion de l'autophagie
    x_tete = int(canvas.coords(corp_snake)[0] // COTE)
    y_tete = int(canvas.coords(corp_snake)[1] // COTE)
    if tableau_snake[y_tete][x_tete] == 1 :
        game_over()
        return
    tableau_snake[y_tete][x_tete] = 1
    # Gestion entre le pomme et le serpent
    if x_tete == x_pomme and y_tete == y_pomme :
        # ===========================
        # A FAIRE : Déplacer la pomme
        # exemple : deplacer_pomme()
        # ===========================
        snake_grandit(x_queue, y_queue)
    # Rappel la fonction move_snake
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

def game_over(event=0) :
    """Fonction qui affiche une Game Over quand le joueur perd et réinitialiser toutes les variable globals"""
    global tableau_snake, snake, tete_snake, corp_snake, direction, pomme, ID_after
    # Affiche le game over
    canvas.create_image(500/2, 500/2, anchor='center', image=image_GO)
    # Effacer le serpent et la pomme
    canvas.delete(pomme)
    for i in snake :
        canvas.delete(i)
    # Réinitialiser les variable global, A FAIRE : ajout des variable des future fonctions pour tout réinitialiser
    tableau_snake = [[0] * COLONE for i in range(LIGNE)]
    snake = []
    tete_snake = 0
    corp_snake = 0
    direction = ["droite", +COTE, 0]
    pomme = 0
    ID_after = 0

#######################################
# Programme principale

racine = Tk()
racine.title("Snake")

# Création des widgets

canvas = Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="green")
image_GO = PhotoImage(file='gameover.png')

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
