#Début de partie
def debut(taille):
	mat=[]
	for i in range(taille):
		mat.append([])
	for j in range(taille):
		for i in range(taille):
			mat[j].append(0)
	return mat


#pas de case vide
def pasvide(mat,taille=4):
	pasvide=True
	for i in range(taille):
		for j in range(taille):
			if mat[i][j]==0:
				pasvide=False
				break
	return pasvide

	
#pas de voisin horizontale
def pashorizontal(mat,taille=4):
	pashorizontal=True
	for i in range(taille):
		for j in range(taille-1):
			if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
				pashorizontal=False
				break
	return pashorizontal


#pas de voisin verticale
def pasverticale(mat,taille=4):
	pasverticale=True
	for j in range(taille):
		for i in range(taille-1):
			if mat[i][j]==mat[i+1][j] and mat[i][j]!=0:
				pasverticale=False
				break
	return pasverticale


#Conditions pour perdre au jeu
def perdre(mat,taille=4):
	perdu=False	
	if pasvide(mat,taille) and pashorizontal(mat,taille) and pasverticale(mat,taille):
		perdu=True
		return perdu

		
#Conditions pour gagner au jeu
def gagner(mat,taille=4,but=11):
	gagner=False
	for i in range(taille):
		for j in range(taille):
			if mat[i][j]==but:
				gagner=True
				break
	return gagner
	
	
#bonne touche
def touche(saisie):
	touche=False
	if saisie=='q':
		touche=True
	if saisie=='s':
		touche=True
	if saisie=='d':
		touche=True
	if saisie=='z':
		touche=True
	if saisie=='0':
		touche=True
	return touche

	
#Continuer de jouer
def continuer(mat,taille=4):
	continuer=True
	if gagner(mat,taille):
		continuer=False
	if perdre(mat,taille):
		continuer=False
	return continuer