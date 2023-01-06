family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
family_cost = 0
for name, age in family.items():
  cost = 0
  if age < 3:
    cost = 0
  elif age < 12:
    cost = 10
  else:
    cost = 15
  family_cost += cost
  print(f"{name} doit payer {cost} $")

print(f"Le coût total de la famille pour les films est de {family_cost} $")


    