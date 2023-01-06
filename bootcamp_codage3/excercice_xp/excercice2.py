family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
S=0
V=0
liste=[]
name=input("Votre nom:")
if  name=="rick" and name=="beth":
    S=S+15
    liste=name.split()
    print("chacun doit payer 15 dollars")
elif name=='morty' and name=='summer':
    V=V+10
    liste=name.split()
    print('chacun doit payer 10 dollars')
print("la somme total est de:",S+V)    

    
    