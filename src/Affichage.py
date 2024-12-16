#Puissance de deux
def powerdeux(chiffre):
	puissance=1
	for i in range(chiffre):
		puissance=puissance*2
	return puissance


#Determiner quoi mettre à l'intérieur du carré
def remplir(chiffre):
	if chiffre!=0:
		nombre=powerdeux(chiffre)
		if len(str(nombre))==1:
			ligne="  "+str(nombre)+" "
			return ligne
		if len(str(nombre))==2:
			ligne=" "+str(nombre)+" "
			return ligne
		if len(str(nombre))==3:
			ligne=str(nombre)+" "
			return ligne
		if len(str(nombre))==4:
			ligne=str(nombre)
			return ligne
		if len(str(nombre))>4:
			ligne="2^"+chiffre
	else:
		ligne="    "
		return ligne


#Apparence du 2048
def Graphic(mat,taille=4,score=0):
	print()
	print("                      Score:",score)
	print(' ',end='')
	print("-------"*taille,end='')
	print('-')
	for i in range(taille):
		print(' ',end='')
		print("l      "*taille,end='')
		print("l")
		for j in range(taille):
			print(" l",remplir(mat[i][j]),end='')
		print(' l')
		print(' ',end='')
		print("l      "*taille,end='')		
		print("l")
		print(' ',end='')
		print("-------"*taille,end='')
		print('-')

