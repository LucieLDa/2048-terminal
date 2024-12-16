import sys
import os
import pickle
from Affichage import *
from mouvements import *
from gagnerperdre import *
os.system('cls')


#Choix du joueur
choix='0'
taille=input("Taille du jeu")
try:
	taille=int(taille)
	assert taille>3
except ValueError:
	print("Veuillez ne pas saisir n'importe quoi!")
	sys.exit(0) 
except AssertionError:
	print("Le nombre saisie est inférieur à 4")
	sys.exit(0) 

#Avant le jeu
score=0
but=taille*taille-(5*(taille-3))
print("Objectif: Ateindre le nombre",powerdeux(but),",soit 2 puissance",but,end='')
print('!')
jeu=debut(taille)
jeu=vide(jeu,taille)

#Pendant le jeu
while continuer(jeu,taille):
	if pasvide(jeu,taille)==False and touche(choix)==True:
		jeu=vide(jeu,taille)
	os.system('cls')
	Graphic(jeu,taille,score)
	print("QZDS pour direction, 0 pour quitter")
	choix=input("Direction?")
	if choix=='q':	
		tableau=tgauche(jeu,taille,score)
		score=tableau[0]
		mat=tableau[1]
	if choix=='z':
		tableau=thaut(jeu,taille,score)
		score=tableau[0]
		mat=tableau[1]
	if choix=='s':
		tableau=tbas(jeu,taille,score)
		score=tableau[0]
		mat=tableau[1]
	if choix=='d':
		tableau=tdroit(jeu,taille,score)
		score=tableau[0]
		mat=tableau[1]
	if choix=='0':
		break

		
#Fin du jeu
if gagner(jeu,taille):
	Graphic(jeu)	
	print("GAGNER")

if perdre(jeu,taille):
	Graphic(jeu)
	print("PERDU")

#Highscore
with open('Highscore', 'rb') as fichier:
	mon_depickler = pickle.Unpickler(fichier)
	score_recupere = mon_depickler.load()

for i in range(4):
	print(score_recupere[i])

for i in range(5):
	if score_recupere[-i][1]<score:
		print("felicitation")
		print("Enregistrer votre score? 1 oui/0 non")
		choix=int(input())
		if choix==1:
			score_recupere[-i][0]=input("votre nom")
			score_recupere[-i][1]=score
			for j in range(4):
				for f in range (3):
					if score_recupere[f][1]<score_recupere[f+1][1]:
						d=score_recupere[f]
						e=score_recupere[f+1]
						score_recupere[f+1]=d
						score_recupere[f]=e
			os.system('cls')
			for m in range(4):
				print(score_recupere[m])	
		break


with open('Highscore', 'wb') as fichier:
	mon_pickler = pickle.Pickler(fichier)
	mon_pickler.dump(score_recupere)

