n=input("entrer une série de garnitures de pizza:")
list=[]
S=0
v="quitter"
while n!=v:
    n=input("entrer une série de garnitures de pizza:")
    print("vous avez ajouter"+n+ "et"" de pizza")
    list.append(n)
    S=S+2.5   
print(list)
print("le prix total est de: ",10+S)

