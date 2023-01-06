number = int(input("Veuillez entrer un nombre : "))
length = int(input("Veuillez entrer la longueur de la liste : "))

# Initialisez la liste avec le premier multiple de number
multiples = [number]

# Utilisez une boucle while pour ajouter les multiples suivants à la liste
# jusqu'à ce que la longueur de la liste atteigne length
i = 2
while len(multiples) < length:
  multiple = number * i
  multiples.append(multiple)
  i += 1

print(multiples)
