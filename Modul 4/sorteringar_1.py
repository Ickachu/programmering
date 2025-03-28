from random import randrange # endast hämta funktionen randrange från modulen random 
lista = [randrange(1,101) for i in range (20)] # skapar lista av 20 slumpade heltal inom spannet 1-100
print(lista) # utskrift av listan
mintal = lista[0] # variabeln mintal tilldelas ett värde som endast är en utgångspunkt för att kunna jämföra med resten av listan: man måste gissa på att något är lägst
plats = 0 # samma som ovan: en utgångspunkt. en variabel vars värde kan ändras

# loopen som ska köras som syftar till att hitta det minsta talet och vilket index det har (spara platsen talet har)
for i in range (1, len(lista)): # loop som ökar referenspunkt med 1 varje upprepning
    if lista[i] < mintal: # om index 1 är mindre än mintal (som vi satt som utgångspunkt index 0) 
        mintal = lista[i] # så tilldelas mintal det nya värdet och värdet sparas. Värdet har index 1
        plats = i # Index 1 sparas, vilket alltså innebär att vår variabel -plats- tilldelas det nya indexet 1

print("Minsta tal = {} på plats {}".format(mintal, plats)) # använd {} för att infoga variabler som skrivs inom parentes efter .format



# låter programmet byta värden på indexen: index 0 och indexet för det verkliga minsta talet
# -----------------------------
# ^                           v
lista[0], lista[plats] = lista[plats], lista[0]  # det första innan tildelningstecknet byter värde med det första efter tilldelningstecknet, vice versa
#                 v                     ^
#                 -----------------------

 
print("Sedan vi bytt plats på första och minsta:")
print(lista) # kontrollutskrift


