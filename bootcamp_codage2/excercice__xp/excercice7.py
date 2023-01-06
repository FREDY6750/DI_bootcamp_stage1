fruits=input("saisir nom de/des Fruits prefere(s) separer par un espace:")
liste=fruits.split()
fruit=input("entrer le nom d'un fruit:")
if fruit in liste:
    print("Vous avez choisi l'un de vos fruits préférés ! Prenez plaisir!:")
else:
    print("Vous avez choisi un nouveau fruit. J'espère que tu apprécies")    
    