from random import randrange 
from time import time

def urvalssort(lista):
    for j in range(len(lista)-1): # första raden yttre loop
        mintal = lista[j] # yttre loop
        plats = j # yttre loop
        for i in range(j+1, len(lista)): # inre loop
            if lista[i] < mintal: # inre loop
                mintal = lista[i] # inre loop
                plats = i # inre loop
        lista[j], lista[plats] = lista[plats], lista[j]

# först fråga efter antal tal att slumpa och sortera,
# sedan tar vi tid på sorteringen och skriver ut
antal = int(input("Hur många tal vill du sortera? "))
lista = [randrange(1,101) for i in range (antal)] # slumpa fram lista med 20 tal
t0 = time()
urvalssort(lista)
t1 = time()
print("Att sortera {:d} heltal tog {:.3f}\sekunder".format(antal, t1 - t0))