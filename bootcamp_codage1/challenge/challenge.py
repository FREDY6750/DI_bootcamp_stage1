string = input("Veuillez entrer une chaîne de 10 caractères : ")

if len(string) < 10:
  print("chaîne pas assez longue")
elif len(string) > 10:
  print("chaîne trop longue")
else:
  print("La chaîne a 10 caractères.")
print("Le premier caractère est :", string[0])
print("Le dernier caractère est :", string[-1])
for character in string:
  print(character)
