# Projet_Snake

L'objectif de ce projet est de programmer le jeu "Snake".

## Description de Snake

Ce jeu est composé d'une grille. Chaque case contient au choix :
- Des murs
- Un bout de serpent
- Une pomme
- De l'herbe

## Principe du Snake

À intervalle régulier, le serpent avance. Le joueur peut contrôler sa direction à l'aide des touches du clavier suivantes :
- Direction "Haut" : touche "z"
- Direction "Bas" : touche "s"
- Direction "Gauche" : touche "q"
- Direction "Droite" : touche "d"

Le but est de manger la pomme. Lorsqu'elle est mangée, une autre pomme apparaît sur une case aléatoire du plateau, et la longueur du serpent augmente de 1.

La partie s'arrête lorsque la tête du serpent percute un mur ou percute son propre corps.

## Clone du Projet

On doit récupérer les fichiers suivants :
- Les 10 meilleurs scores.txt
- README.md
- Snake_FilinaDERIAN_SarahGUERFA_LiciaBENKHEROUF_PaulineSTAELENS.py 
- Snake_difficult.txt
- Snake_easy.txt
- Snake_intermédiate.txt
- gameover.png
- snake.png

## Fonctionnalité

Pour lancer le programme exécuter le fichier "Snake_FilinaDERIAN_SarahGUERFA_LiciaBENKHEROUF_PaulineSTAELENS.py"

Avant de lancer une partie, le joueur a accès à un menu.

Le joueur est invité à entrer un pseudo.

Il peut choisir entre 3 niveaux de difficulté différents :
- le niveau "Facile", un plateau grand avec 4 murs sur les côtés et avec une vitesse du serpent lente ;
- le niveau "Intermédiaire", un plateau moyen avec 4 murs sur les côtés, 2 murs au milieu et avec une vitesse du serpent moyenne ;
- le niveau "Difficile", un plateau petit avec 4 murs sur les côtés, 4 murs au milieu et avec une vitesse du serpent rapide.

Le plateau apparaît dans une nouvelle fenêtre et le serpent commence à avancer.

Le score est affiché pendant la partie et augment de 10 points pour chaque pomme que le serpent mange.

Pour recommencer une partie après un "Game Over", il suffit de fermer la fenêtre du plateau de jeu et de rechoisir un niveau.

Le joueur peut consulter les 10 meilleurs scores dans le menu.

## Remarque

On a rencontré des problèmes sur le placement des boutons du menu, on suppose que selon le système d'exploitation de votre ordinateur (windows, Linux, IOS...) les boutons sont mal placés dans la fenêtre du menu du jeu. Les boutons se chevauchent et peuvent gêner le lancement du niveau intermédiaire.

Le visuel que vous devait avoir est le suivant : 
 
![menu du jeu](https://user-images.githubusercontent.com/71285109/119358057-86618e00-bca8-11eb-996f-6811ed6bfddc.png)

Le visuel qu'il est possible d'avoir est le suivant :
(c'est un exemple)

![menu du jeu avec les boutons qui se chevauchent](https://user-images.githubusercontent.com/71285109/119348250-e5210a80-bc9c-11eb-8a8f-e85f5b36c2af.png)
