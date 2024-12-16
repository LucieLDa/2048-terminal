import random 
from Affichage import *

#Lorsque 2 chiffres à l'horizontale sont les mêmes droite
def horizond(mat,taille=4,score=0):
	for i in range(1,taille+1):
		for j in range(1,taille):
			if mat[-i][-j]==mat[-i][-j-1] and mat[-i][-j]!=0:
				mat[-i][-j-1]=0
				mat[-i][-j]=mat[-i][-j]+1
				score=score+powerdeux(mat[-i][-j])
	valeurs=[score,mat]
	return valeurs

#Mettre tout à droite
def droite(mat,taille=4):
	for i in range(taille):
		c=0
		for j in range(1,taille+1):
			if mat[i][-j]==0:
				for t in range(2+c,taille+1):
					if mat[i][-t]!=0 and mat[i][-j]==0:
						mat[i][-j]=mat[i][-t]
						mat[i][-t]=0				
			c=c+1
	return mat

#Lorsqu'on fait touche droit
def tdroit(mat,taille=4,score=0):
	resultat=droite(mat,taille)
	tableau=horizond(mat,taille,score)
	resultat=tableau[1]
	score=tableau[0]
	resultat=droite(mat,taille)
	valeurs=[score,resultat]
	return valeurs

	
#Lorsque 2 chiffres à l'horizontale sont les mêmes gauche
def horizong(mat,taille=4,score=0):
	for i in range(taille):
		for j in range(taille-1):
			if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
				mat[i][j+1]=0
				mat[i][j]=mat[i][j]+1
				score=score+powerdeux(mat[i][j])
	valeurs=[score,mat]
	return valeurs
	
#Mettre tout à gauche
def gauche(mat,taille=4):
	for i in range(taille):
		c=0
		for j in range(taille):
			if mat[i][j]==0:
				for t in range(c+1,taille):
					if mat[i][t]!=0 and mat[i][j]==0:
						mat[i][j]=mat[i][t]
						mat[i][t]=0
			c=c+1
	return mat
	
#Lorsqu'on fait touche gauche
def tgauche(mat,taille=4,score=0):
	resultat=gauche(mat,taille)
	tableau=horizong(mat,taille,score)
	resultat=tableau[1]
	score=tableau[0]	
	resultat=gauche(mat,taille)
	valeurs=[score,resultat]
	return valeurs

	
#Lorsque 2 chiffres à la verticale sont les mêmes bas
def verticaleb(mat,taille=4,score=0):
	for j in range(1,taille+1):
		for i in range(1,taille):
			if mat[-i][-j]==mat[-i-1][-j] and mat[-i][-j]!=0:
				mat[-i-1][-j]=0
				mat[-i][-j]=mat[-i][-j]+1
				score=score+powerdeux(mat[-i][-j])
	valeurs=[score,mat]
	return valeurs

#Mettre tout en bas
def bas(mat,taille=4):
	for j in range(taille):
		c=0
		for i in range(1,taille+1):
			if mat[-i][j]==0:
				for t in range(2+c,taille+1):
					if mat[-t][j]!=0 and mat[-i][j]==0:
						mat[-i][j]=mat[-t][j]
						mat[-t][j]=0
			c=c+1
	return mat

#Lorsqu'on fait touche bas
def tbas(mat,taille=4,score=0):
	resultat=bas(mat,taille)
	tableau=verticaleb(mat,taille,score)
	resultat=tableau[1]
	score=tableau[0]	
	resultat=bas(mat,taille)
	valeurs=[score,resultat]
	return valeurs

	
#Lorsque 2 chiffres à la verticale sont les mêmes haut
def verticaleh(mat,taille=4,score=0):
	for j in range(taille):
		for i in range(taille-1):
			if mat[i][j]==mat[i+1][j] and mat[i][j]!=0:
				mat[i+1][j]=0
				mat[i][j]=mat[i][j]+1
				score=score+powerdeux(mat[i][j])
	valeurs=[score,mat]
	return valeurs
	
#Mettre tout en haut
def haut(mat,taille=4):
	for j in range(taille):
		c=0
		for i in range(taille):
			if mat[i][j]==0:
				for t in range(c+1,taille):
					if mat[t][j]!=0 and mat[i][j]==0:
						mat[i][j]=mat[t][j]
						mat[t][j]=0
			c=c+1
	return mat
	
#Lorsqu'on fait touche haut
def thaut(mat,taille=4,score=0):
	resultat=haut(mat,taille)
	tableau=verticaleh(mat,taille,score)
	resultat=tableau[1]
	score=tableau[0]	
	resultat=haut(mat,taille)
	valeurs=[score,resultat]
	return valeurs


#Mettre un 1 ou 2 au hasard dans une case vide
def vide(mat,taille=4):
	k=0
	while k==0:
		i=random.randint(0,taille-1)
		j=random.randint(0,taille-1)
		if mat[i][j]==0:
			k=random.randint(1,5)
			if k==1:
				mat[i][j]=2
			else:
				mat[i][j]=1
			break
	return mat
	
