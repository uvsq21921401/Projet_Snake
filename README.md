# Projet_Snake

L'objectif de ce projet est de programmer le jeu "Snake".

## Description de Snake

Ce jeu est composé d'une grille. Chaque case contient au choix :
- Des murs
- Un bout de serpent
- Une pomme
- De l'herbe

## Principe du Snake

À intervalle régulier, le serpent avance. Le joueur peut contrôler sa direstion à l'aide des touches du clavier suivantes :
- Direction "Haut" : touche "z"
- Direction "Bas" : touche "s"
- Direction "Gauche" : touche "q"
- Direction "Droite" : touche "d"

Le but est de manger la pomme. Lorsqu'elle est mangé, une autre pomme apparaît sur une case aléatoire du plateau, et la longueur du serpent augmente de 1.

La partie s'arrête lorsque la tête du serpent percute un mur ou percute son propre corps.

## Fonctionnalité

Avant de lancer une partie, le joueur a accés à un menu.

Le joueur est invité à entrer un pseudo.

Il peut choisir entre 3 niveaux de difficulté différente :
- le niveau "Facile", c'est un plateau grand avec 4 murs sur les côtes et la vitesse du serpent est lente ;
- le niveau "Intermédiaire", c'est un plateau moyen avec 4 murs sur les côtes, plus 2 murs au milieu et la vitesse du serpent est moyenne ;
- le niveau "Difficile", c'est un plateau petit avec 4 murs sur les côtes, plus 4 murs au milieu et la vitesse du serpent est rapide.

Le plateau appareil dans une nouvelle fenêtre et le serpent commence à avancer.

Le score est affiché pendant la partie et auguement de 10 points pour chaque pomme que le serpent mange.

Pour recommencer une partie aprés un "Game Over", il suffit de fermer la fenêtre du plateau de jeu et de rechoisir un niveau.

Le joueur peut consulter les 10 meilleurs scores dans le menu.
