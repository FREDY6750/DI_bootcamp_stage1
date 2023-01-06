liste=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
indice=[]
for i in range (len(liste) + 1):
    if (i%2==0):
        indice.append(i)
print(indice)