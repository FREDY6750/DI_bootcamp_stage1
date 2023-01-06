liste=[]
V=0 
S=0
a=-1
m=int(input("entrez votre age:"))
while m!=-1:
    m=int(input("entrez votre age:"))
    if m<3:
        print("vous avez un ticket gratuit")
    elif m>3 and m<12:
        V=V+10
        print("le billet est de 10 dollars")
    elif m>12:
        S=S+15
        print("le billet est de 15 dollars")
        liste.append(m)
print(liste)
print('le cout total est de:',S+V)