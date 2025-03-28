# ta bort kontrollutskrift av att ha hittat minsta tal
# gör yttre loop där vi upprepar samma sak med de återstående talen tills hela listan är sorterad
# på slutet skriva ut den sorterade listan

from random import randrange 

lista = [randrange(1,101) for i in range(20)]

for j in range(len(lista)-1): # första raden yttre loop
    mintal = lista[j] # yttre loop
    plats = j # yttre loop
    for i in range(j+1, len(lista)): # inre loop
        if lista[i] < mintal: # inre loop
            mintal = lista[i] # inre loop
            plats = i # inre loop

    lista[j], lista[plats] = lista[plats], lista[j] # sista raden yttre loop

print("Sorterad lista:")
print(lista)


# gör en funktion av programmet: utför endast sorteringen och gör inte kontrollutskrifter

def urvalssort(lista):
    for j in range(len(lista)-1): # första raden yttre loop
    mintal = lista[j] # yttre loop
    plats = j # yttre loop
        for i in range(j+1, len(lista)): # inre loop
        if lista[i] < mintal: # inre loop
            mintal = lista[i] # inre loop
            plats = i # inre loop
        lista[j], lista[plats] = lista[plats], lista[j]
    
### SLUTLIGA HUVUDPROGRAMMET 

from random import randrange 

def urvalssort(lista):
    for j in range(len(lista)-1): # första raden yttre loop
    mintal = lista[j] # yttre loop
    plats = j # yttre loop
        for i in range(j+1, len(lista)): # inre loop
            if lista[i] < mintal: # inre loop
            mintal = lista[i] # inre loop
            plats = i # inre loop
        lista[j], lista[plats] = lista[plats], lista[j]
    
lista = [randrange(1,101) for i in range (20)]
print(lista)
urvalssort(lista)
print("Sorterad lista:")
print(lista)
