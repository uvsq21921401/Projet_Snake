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
import random

#######################################
# Constantes

COTE = 20

COLOR_QUADR = "black"
COLOR_MUR = "black"
COLOR_MUR_BORD = "green"
COLOR_POMME = "red"
COLOR_TETE_SNAKE = "Cyan3"
COLOR_SNAKE = "Green2"

#######################################
# Variables globales

largeur = 0
hauteur = 0
colone = 0
ligne = 0

tableau_mur = []
tableau_snake = []

snake = []
tete_snake = 0
corp_snake = 0
direction = ["droite", +COTE, 0]
vitesse = 0

pomme = 0
score = 0
pseudo = ""

ID_after = 0
canvas = 0
label_score = 0

fichier = 0
nom_fichier = 0

#######################################
# Fonctions

def read_fichier(nom_fichier) :
    """Lit un fichier txt pour les attribuer a une variable global"""
    global largeur, hauteur, colone, ligne, vitesse, tableau_mur, fichier
    fichier = open(nom_fichier, "r")
    largeur = int(fichier.readline())
    hauteur = int(fichier.readline())
    colone = largeur // COTE
    ligne = hauteur // COTE
    vitesse = int(fichier.readline())
    for i in range(hauteur//COTE) :
        tableau_mur.append([])
        line = fichier.readline()
        for j in line :
            if j != '\n' :
                tableau_mur[i].append(int(j))
    fichier.close()

def quadrillage():
    """Dessine un quadrillage formé de carrés de côté COTE (fonction pour nous aider a bien visualise le deplacement de la pomme et du serpent)"""
    global hauteur, largeur, COTE, COLOR_QUADR
    y = 0
    while y <= hauteur:
        canvas.create_line((0, y), (largeur, y), fill=COLOR_QUADR)
        y += COTE
    x = 0
    while x <= largeur:
        canvas.create_line((x, 0), (x, hauteur), fill=COLOR_QUADR)
        x += COTE

def ini_mur() :
    """Créer des carré noir de dimention COTE pour créer les murs"""
    global tableau_mur, COTE, COLOR_MUR, COLOR_MUR_BORD
    for i in range(len(tableau_mur)) :
        for j in range(len(tableau_mur[i])) :
            if tableau_mur[i][j] == 1 :
                canvas.create_rectangle((j*COTE, i*COTE), ((j+1)*COTE, (i+1)*COTE), fill=COLOR_MUR, outline=COLOR_MUR_BORD)

def position_depart() :
    """Initialise les posistion de départ du serpent et de la pomme"""
    global COTE, largeur, hauteur, pomme, tete_snake, corp_snake, snake, tableau_snake, COLOR_POMME, COLOR_TETE_SNAKE, COLOR_SNAKE
    # Position de départ de la pomme
    pomme = canvas.create_oval( (largeur-(4*COTE), hauteur-(4*COTE)), (largeur-(3*COTE), hauteur-(3*COTE)), fill=COLOR_POMME, outline=COLOR_POMME)
    # Position de départ du serpent
    tableau_snake = [[0] * colone for i in range(ligne)] 
    tete_snake = canvas.create_oval((4*COTE, 2*COTE), (5*COTE, 3*COTE), fill=COLOR_TETE_SNAKE, outline=COLOR_TETE_SNAKE)
    snake.append(tete_snake)
    tableau_snake[2][4] = 1
    corp_snake = canvas.create_oval((3*COTE, 2*COTE), (4*COTE, 3*COTE), fill=COLOR_SNAKE, outline=COLOR_SNAKE)
    snake.append(corp_snake)
    tableau_snake[2][3] = 1
    corp_snake = canvas.create_oval((2*COTE, 2*COTE), (3*COTE, 3*COTE), fill=COLOR_SNAKE, outline=COLOR_SNAKE)
    snake.append(corp_snake)
    tableau_snake[2][2] = 1

def move_pomme() :
    """Déplace la pomme quand elle se fait manger par le serpent"""
    global pomme, colone, ligne, COTE, tableau_mur, tableau_snake, score, label_score
    x = random.randint(0, ligne - 1)
    y = random.randint(0, colone - 1)
    coord = x * len(tableau_mur[0]) + y
    while tableau_mur[x][y] == 1 or tableau_snake[x][y] == 1 :
        coord = (coord + 1) % (colone*ligne)
        x = coord // len(tableau_mur[0])
        y = coord % len(tableau_mur[0])
    canvas.coords(pomme, y*COTE, x*COTE, (y+1)*COTE, (x+1)*COTE)
    score += 10
    label_score.config(text="Score: " + str(score))

def snake_grandit(x_queue, y_queue) :
    """Fonction qui ajout un rond au bout du serpent pour le faire grandir"""
    global snake, tableau_snake, corp_snake, COTE, COLOR_SNAKE
    tableau_snake[y_queue][x_queue] = 1
    corp_snake = canvas.create_oval((x_queue*COTE, y_queue*COTE), ((x_queue+1)*COTE, (y_queue+1)*COTE), fill=COLOR_SNAKE, outline=COLOR_SNAKE)
    snake.append(corp_snake)

def move_snake(racine) :
    """Fonction qui deplace le serpent dans une direction (près choisie dans d'autres fonction : move_haut/bas/gauche/bas) en prennant la queue du serpent pour qu'elle devienner sa nouvelle tête"""
    global snake, direction, corp_snake, tete_snake, tableau_snake, COTE, pomme, ID_after, vitesse, tableau_mur, COLOR_TETE_SNAKE, COLOR_SNAKE, largeur, hauteur
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
    canvas.coords(corp_snake, (canvas.coords(tete_snake)[0] + direction[1]) % largeur, (canvas.coords(tete_snake)[1] + direction[2]) % hauteur, (canvas.coords(tete_snake)[0] + direction[1] + 19) % largeur, (canvas.coords(tete_snake)[1] + direction[2] + 19) % hauteur)
    canvas.itemconfigure(snake[-1], fill=COLOR_TETE_SNAKE, outline=COLOR_TETE_SNAKE)
    canvas.itemconfigure(snake[0], fill=COLOR_SNAKE, outline=COLOR_SNAKE)
    snake.insert(0, snake[-1])
    del snake[-1]
    # Gére la position de serpent dans le tableau_snake aprés deplacement + Gestion de l'autophagie et rentre dans un mur
    x_tete = int(canvas.coords(corp_snake)[0] // COTE)
    y_tete = int(canvas.coords(corp_snake)[1] // COTE)
    if tableau_snake[y_tete][x_tete] == 1  or tableau_mur[y_tete][x_tete] == 1:
        game_over()
        return
    tableau_snake[y_tete][x_tete] = 1
    # Gestion entre le pomme et le serpent
    if x_tete == x_pomme and y_tete == y_pomme :
        move_pomme()
        snake_grandit(x_queue, y_queue)
    # Rappel la fonction move_snake
    ID_after = racine.after(vitesse, move_snake, racine)

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
    """Fonction qui affiche une Game Over quand le joueur perd"""
    global largeur, hauteur, image_GO, pomme, snake
    canvas.create_image(largeur/2, hauteur/2, anchor='center', image=image_GO)
    canvas.delete(pomme)
    for i in snake :
        canvas.delete(i)
    score_joueur()

def score_joueur() :
    global score, pseudo
    print(pseudo)
    """Fonction qui engistre les information du ficier Les 10 meilleurs scores dans un liste et écris le ficher avec le score du joueur si il fait partie des 10 premier"""
    # lit et stocke les infos du fichier
    liste_score = [[""] * 2 for i in range(10)]
    fichier_S = open("Les 10 meilleurs scores.txt", "r")
    fichier_S.readline()
    for i in range(len(liste_score)) :
        line = fichier_S.readline()
        split = line.split(" ")
        liste_score[i][0], liste_score[i][1] = split[1], int(split[2]) 
    fichier_S.close()
    # réecrit les infos du fichier selon la position du score du joueur
    ins = trier_score(liste_score, score)
    liste_score.insert(ins, [pseudo, score])
    fichier_S = open("Les 10 meilleurs scores.txt", "w")
    fichier_S.write("Les 10 meilleurs scores" + "\n")
    for i in range(10) :
        fichier_S.write(str(i+1) + " " + liste_score[i][0] + " " + str(liste_score[i][1]) + " " + "\n")
    fichier_S.close()

def trier_score (liste_score, score) :
    """Fonction qui compare le score du joueur par rapport aux scores du fichier Les 10 meilleurs scores pour le classe dans les 10 premiere place et retoune la possition pour la fonction score_joueur"""
    for i in range(len(liste_score)) :
        if liste_score[i][1] <= score :
            return i
    return 10

def save_pseudo (variable) :
    """Fonction qui enregistre le pseudo du joueur"""
    global pseudo
    pseudo = variable.get()

def reinitialise_variableG() :
    """Réinitialiser les variable global"""
    global largeur, hauteur, colone, ligne, tableau_mur, tableau_snake, snake, tete_snake, corp_snake, direction, vitesse, pomme, score, ID_after, canvas, label_score, fichier, nom_fichier, COTE
    if canvas != 0 : 
        largeur = 0
        hauteur = 0
        colone = 0
        ligne = 0
        tableau_mur = []
        tableau_snake = []
        snake = []
        tete_snake = 0
        corp_snake = 0
        direction = ["droite", +COTE, 0]
        vitesse = 0
        pomme = 0
        score = 0
        ID_after = 0
        canvas = 0
        label_score = 0
        fichier = 0
        nom_fichier = 0

#######################################
# Programme Menu 

# Fenêtre des différents niveaux
def create1():
    """Fonction qui créée une nouvelle fenetre pour le niveau facile et appele les fonctions pour le bon fonctionnement du jeu"""
    global canvas, largeur, hauteur, nom_fichier, image_GO, score, label_score
    easy=tk.Tk()
    easy.title("Niveau Facile")
    easy.geometry('805x430')
    easy.configure(bg='#88e75f')
    easy.resizable(False, False)
    # Appele de fonction pour initialiser de l'espace de jeu
    reinitialise_variableG()
    save_pseudo(variable)
    nom_fichier = "Snake_easy.txt"
    read_fichier(nom_fichier)
    # Création des widgets
    canvas = tk.Canvas(easy, width=largeur, height=hauteur, bg="green")
    label_score = tk.Label(easy, text="Score: " + str(score), bg = "#88e75f")
    image_GO = tk.PhotoImage(file='gameover.png', master=easy)
    # Placement des widgets
    canvas.grid(row=0)
    label_score.grid(row=1)
    # Appele de fonction pour jouer
    ##quadrillage()
    ini_mur()
    position_depart()
    racine = easy
    move_snake(racine)
    # Èvenement
    easy.bind("<KeyPress-z>", move_haut)
    easy.bind("<KeyPress-s>", move_bas)
    easy.bind("<KeyPress-q>", move_gauche)
    easy.bind("<KeyPress-d>", move_droite)
    
    easy.mainloop()

def create2():
    """Fonction qui créée une nouvelle fenetre pour le niveau intermédiaire et appele les fonctions pour le bon fonctionnement du jeu"""
    global canvas, largeur, hauteur, nom_fichier, image_GO, score, label_score
    intermediate=tk.Tk()
    intermediate.title("Niveau Intermédiaire")
    intermediate.geometry('605x430')
    intermediate.configure(bg='#88e75f')
    intermediate.resizable(False, False)
    # Appele de fonction pour initialiser de l'espace de jeu
    reinitialise_variableG()
    save_pseudo(variable)
    nom_fichier = "Snake_intermédiate.txt"
    read_fichier(nom_fichier)
    # Création des widgets
    canvas = tk.Canvas(intermediate, width=largeur, height=hauteur, bg="green")
    label_score = tk.Label(intermediate, text="Score: " + str(score), bg = "#88e75f")
    image_GO = tk.PhotoImage(file='gameover.png', master=intermediate)
    # Placement des widgets
    canvas.grid(row=0)
    label_score.grid(row=1)
    # Appele de fonction pour jouer
    ##quadrillage()
    ini_mur()
    position_depart()
    racine = intermediate
    move_snake(racine)
    # Èvenement
    intermediate.bind("<KeyPress-z>", move_haut)
    intermediate.bind("<KeyPress-s>", move_bas)
    intermediate.bind("<KeyPress-q>", move_gauche)
    intermediate.bind("<KeyPress-d>", move_droite)

    intermediate.mainloop()

def create3():
    """Fonction qui créée une nouvelle fenetre pour le niveau intermédiaire et appele les fonctions pour le bon fonctionnement du jeu"""
    global canvas, largeur, hauteur, nom_fichier, image_GO, score, label_score
    difficult=tk.Tk()
    difficult.title("Niveau Difficile")
    difficult.geometry('405x430')
    difficult.configure(bg='#88e75f')
    difficult.resizable(False, False)
    # Appele de fonction pour initialiser de l'espace de jeu
    reinitialise_variableG()
    save_pseudo(variable)
    nom_fichier = "Snake_difficult.txt"
    read_fichier(nom_fichier)
    # Création des widgets
    canvas = tk.Canvas(difficult, width=largeur, height=hauteur, bg="green")
    label_score = tk.Label(difficult, text="Score: " + str(score), bg = "#88e75f")
    image_GO = tk.PhotoImage(file='gameover.png', master=difficult)
    # Placement des widgets
    canvas.grid(row=0)
    label_score.grid(row=1)
    # Appele de fonction pour jouer
    ##quadrillage()
    ini_mur()
    position_depart()
    racine = difficult
    move_snake(racine)
    # Èvenement
    difficult.bind("<KeyPress-z>", move_haut)
    difficult.bind("<KeyPress-s>", move_bas)
    difficult.bind("<KeyPress-q>", move_gauche)
    difficult.bind("<KeyPress-d>", move_droite)

    difficult.mainloop()

def create4():
    """Fonction qui créée une nouvelle fenetre qui affiche des scores"""
    # Programme fenetre
    meill_score = tk.Tk()
    meill_score.title("Meilleurs Scores")
    meill_score.geometry('250x250')
    meill_score.configure(bg='#88e75f')
    # Lit le ficher Les 10 meilleurs scores pour les enregistre dans une liste 
    liste_score = [[""] * 2 for i in range(10)]
    fichier_S = open("Les 10 meilleurs scores.txt", "r")
    titre = fichier_S.readline()
    for i in range(len(liste_score)) :
        line = fichier_S.readline()
        split = line.split(" ")
        liste_score[i][0], liste_score[i][1] = split[1], split[2]
    fichier_S.close()
    # Création des widgets
    lab_titre = tk.Label(meill_score, text=titre, bg = "#88e75f")
    lab_1 = tk.Label(meill_score, text="1. " + liste_score[0][0] + " : " + liste_score[0][1] + " points", bg = "#88e75f")
    lab_2 = tk.Label(meill_score, text="2. " + liste_score[1][0] + " : " + liste_score[1][1] + " points", bg = "#88e75f")
    lab_3 = tk.Label(meill_score, text="3. " + liste_score[2][0] + " : " + liste_score[2][1] + " points", bg = "#88e75f")
    lab_4 = tk.Label(meill_score, text="4. " + liste_score[3][0] + " : " + liste_score[3][1] + " points", bg = "#88e75f")
    lab_5 = tk.Label(meill_score, text="5. " + liste_score[4][0] + " : " + liste_score[4][1] + " points", bg = "#88e75f")
    lab_6 = tk.Label(meill_score, text="6. " + liste_score[5][0] + " : " + liste_score[5][1] + " points", bg = "#88e75f")
    lab_7 = tk.Label(meill_score, text="7. " + liste_score[6][0] + " : " + liste_score[6][1] + " points", bg = "#88e75f")
    lab_8 = tk.Label(meill_score, text="8. " + liste_score[7][0] + " : " + liste_score[7][1] + " points", bg = "#88e75f")
    lab_9 = tk.Label(meill_score, text="9. " + liste_score[8][0] + " : " + liste_score[7][1] + " points", bg = "#88e75f")
    lab_10 = tk.Label(meill_score, text="10. " + liste_score[9][0] + " : " + liste_score[9][1] + " points", bg = "#88e75f")
    # Placement des widgets
    lab_titre.place(x = 1, y = 1)
    lab_1.place(x = 1, y = 30)
    lab_2.place(x = 1, y = 50)
    lab_3.place(x = 1, y = 70)
    lab_4.place(x = 1, y = 90)
    lab_5.place(x = 1, y = 110)
    lab_6.place(x = 1, y = 130)
    lab_7.place(x = 1, y = 150)
    lab_8.place(x = 1, y = 170)
    lab_9.place(x = 1, y = 190)
    lab_10.place(x = 1, y = 210)

    meill_score.mainloop()

# Fenêtre du menu

root = tk.Tk()
root.title("Snake")
root.geometry('640x480')
root.resizable(False, False) # bloque la taille de la fenetre
root.configure(bg='#88e75f')

# Création des widgets

menu = tk.Canvas(root, width=640, height=300, bg='#88e75f', highlightthickness=0)
image_menu = tk.PhotoImage(file='snake.png')
image_GO = tk.PhotoImage(file='gameover.png')
menu.create_image(640//2, 300//2, anchor='center', image=image_menu)

label_menu = tk.Label(root, text="Entrez votre Pseudo et choisissez le niveau !", bg = "#88e75f")
variable = tk.StringVar()
entre = tk.Entry(root, textvariable=variable)

btn = tk.Button(root, text="Facile", command = create1,  font=("Courrier", 28), bg ="#2f6d35", fg = "#f88f7c")
btn1 = tk.Button(root, text="Intermédiaire", command = create2,  font=("Courrier", 28), bg = "#2f6d35", fg = "#f88f7c")
btn2 = tk.Button(root, text="Difficile", command = create3,  font=("Courrier", 28),bg = "#2f6d35", fg = "#f88f7c")
btn3 = tk.Button(root, text="Meilleurs Scores", command = create4,  font=("Courrier", 28),bg = "#2f6d35", fg = "#f88f7c")

# Placement des widgets

menu.place(x = 0, y = 0)
label_menu.place(x = 150, y = 290)
entre.place(x = 180, y = 315)
btn.place(x = 80, y = 350)
btn1.place(x = 195, y = 350)
btn2.place(x = 400, y = 350)
btn3.place(x = 180, y = 400)

root.mainloop()
