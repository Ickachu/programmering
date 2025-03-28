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
    
lista = [randrange(1,101) for i in range (20)] # slumpa fram lista med 20 tal
print(lista) # skriva ut osorterad lista
urvalssort(lista) # anropa sorteringsfunktionen
print("Sorterad lista:")
print(lista) # skriva ut sorterade listan som kontroll