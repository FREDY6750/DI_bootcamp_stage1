def supprime_doublons(s):
  # Initialise une variable de sortie vide
  s_nouveau = ""
  # Itère sur chaque caractère de la chaîne d'entrée
  for i in range(len(s)):
    # Si le caractère actuel est différent du précédent, ajoutez-le à la chaîne de sortie
    if i == 0 or s[i] != s[i-1]:
      s_nouveau += s[i]
  # Retourne la chaîne de sortie
  return s_nouveau

# Demande une chaîne à l'utilisateur
s = input("Entrez une chaîne : ")

# Affiche la chaîne avec les caractères consécutifs en double supprimés
print(supprime_doublons(s))
