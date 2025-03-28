# lista är en ordnad samling element som vart och ett kan identifieras med ett index (ett nummer/plats)
# listans element inom hakparenteser

# iteration = upprepning

tal = [12, 15, 36]
tal[0]
12

tecken = ["A", "#", "x", "7"]
tecken[2]
"x"
tecken[3]
"7"

namn = ["Eva", "Anders", "Kalle"]
namn[0]
"Eva"
namn[1]
"Anders"

# elementen behöver inte vara av samma datatyp
a = 5
b = True
lista = [7, "Nisse", 3.14, a ,b]
lista[4]
True
lista[0]
7

# listor av listor
# nedan är en lista av data i en tvådimensionell matris
lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
lista[2]
[7, 8, 9]
lista[1]
[4, 5, 6]
lista[1][2] # index 1 är raden med listelement [4, 5, 6] och index 2 är tredje positionen = 6
6

# man kan ändra, lägga till och ta bort listelement
min_lista = [15, 22, 7, 18, 33]
min_lista[2] = 100 #listelement med index 2 ändras till 100
min_lista
[15, 22, 100, 18, 33]

# lägga till och ta bort element i slutet av lista med metoderna .append() och .pop()
min_lista.append(14)
min_lista
[15, 22, 100, 18, 33, 14] # 14 läggs till i slutet
min_lista.pop() # behöver inte ange sista elementet inom parentes
min_lista 
[15, 22, 100, 18, 33]

# infoga och ta bort element från en viss plats
min_lista.insert(0,5) # på index 0 infoga elementet 5
[5, 15, 22, 100, 18, 33]
min_lista.pop(3) # ta bort element med index 3 = 100
[5, 15, 22, 18, 33]


# loopa igenom en lista med en for-loop eller en while-loop
for tal in min_lista:
    print(tal)

5
15
22
18
33

i = 0
while i < len(min_lista):
    print(min_lista[i])
    i += 1

5
15
22
18
33

# skapa en lista av enstaka tecken av en sträng
1 = list("abc")
1
["a", "b", "c"]


# när man skapar en lista är det lämpligt att initiera den till en tom lista
tal = [] # tom lista
for i in range(1,6):
    tal.append(float(input("Ange tal " + str(i) + ": "))) # input-prompten måste alltid anges som en enda konkatenerad sträng
print("Inmatade tal:")
for x in tal:
    print(x)

# hitta minsta talet i en lista
# det krångliga sättet
tal = [7, 3, 18, 22, 2, 34]
minsta = tal[0] # notera första talet i listan som minst
for i in tal: # loopa igenom resten av listan
    if i < minsta: # om ett tal hittas som är mindre än det redan noterade
        minsta = i # notera det istället
print ("minsta talet är ", minsta)

# det bästa sättet: använda inbyggd funktion i python
tal = [7, 3, 18, 22, 2, 34]
print ("minsta talet är", min(tal))


# tippel/tipplar: en ordnad mängd element. som en lista men oföränderlig (immutable) = kan ej ändra elementen som i en lista
t = (1, 2, 3)
t
(1, 2, 3)
t[1]
2

# tom tippel
t = ()
t
()

# man behöver inte sätta parenteser om en tippel, man kan "packa in" värden 
t = 4,5,6
t
(4, 5, 6)

# "packa upp" samma tippel
a, b, c = t
a
4
b
5
c
6


# byta värde på två variabler genom att använda en temporär variabel
temp = a
a = b
b = temp

# ovanstående kan göras lättare genom att pacla in variablerna i en tippel och sedan packa upp dem i omvänd ordning
a, b = b, a

# skapar en lista och sedan låter en annan variabel referera till denna lista
lista1 = [1, 2, 3, 4]
lista1
[1, 2, 3, 4]
lista2 = lista1
lista2[1, 2, 3, 4]

# en variabel "får liv" så snart den tilldelats ett värde
# en variabel kan referera till None (refereras inte till något men variabeln finns i Pythontolkens lista över variabelnamn)

# skapa en kopia av en lista
# 1a sättet: loopa igenom den ena listan och bygga upp den andra element för element med append()
# 2a sättet: mha en ""list comprehension"
lista2 = [x for x in lista1]
#3e sättet: importera kopieringsmodul och använda funktionen copy() som finns i modulen
import copy
lista2 = copy.copy(lista1) # lista2 blir en äkta kopia av lista1

# kopiera en lista av listor
lista2 = copy.deepcopy(lista1)

# 4e sättet: skapa en slice från det första till det sista elementet i den listan man vill kopiera
lista2 = lista1[:]

# slices av strängar, tipplar eller listor
a = "abcde"
a[2:4]
"cd"
a= (10, 11, 12, 13, 14)
a[1:4]
(11, 12, 13)
a = [4, 5, 6, 7, 8, 9]
a[0:3]
[4, 5, 6]

a = "Kalle Blomkvist"
a[:5] # fram till index 5, men inte inkluderat index 5
"Kalle"
a[6:] # från index 6 till slutet
"Blomkvist"
a[-9:] # vid negativt index räknas det från slutet av litan, strängen eller tippeln
"Blomkvist"

# omvandlingar till lista

# den inbyggda funktionen list() kan användas för att omvandla en sträng eller tippel till en lista
list("Sara")
["S", "a", "r", "a"]
list((1, 2, 3))
[1, 2, 3]

# strängmetoden .split() för att dela upp en sträng i bitar som bildar en lista
s = "Hej på dej du"
s. split("j")
["He", " på de", " du"]

# omvandligar från lista till sträng
# mha strängmetoden .join() kan man av en lista där ALLA element består av strängar bilda en enda lång sträng
s = "Nisse" # sträng
namn = list(s) # göra sträng till lista
namn
["N", "i", "s", "s", "e"]
"__".join(namn) # ange inom "" det/de tecken som ska infogas mellan elementen
"N__i__s__s__e"
"".join(namn) # endast "" om inget tecken ska infogas mellan elementen
"Nisse"

# Repetition: iterera över en sträng eller lista med antingen en for-in-loop eller en while-loop där vi använder indexering
lista = [12, 13, 14, 15]
for tal in lista: # for-in-loop
    print (tal)
12
13
14
15

i = 0
while i z len(lista): # while-loop
    print (lista[i])
    i += 1
12
13
14
15

# göra bägge delarna så att man har tillgång till index samtidigt som man har motsvarande listelement
# mha funktionen enumerate() (räkna upp) som ger en kortade kod samt är effektivare och snabbare i python
s = "Kalle"
for index, tecken in enumerate (s):
    print index, tecken)
0 K
1 a
2 l
3 l
4 e

a = [10, 20, 30, 40]
for x, y in enumerate(a): # för index och tecken i a
    print (x, y) # visa index och tecken
0 10
1 20
2 30
3 40

# ett dictionary = en mängd par där första delen kallas nyckel och den andra delen värde
# varje par kan kalla en post eller ett item
# posterna är inte sorterade på något vis

dict = {nyckel 1:värde 1, nyckel 2:värde 2, ... nyckel n:värde n}

telefon = {"Anders":112233, "Lisa":454545, "Kalle":123456}
telefon
{"Kalle": 123456, "Lisa": 454545, "Anders": 112233}
telefon["Kalle"]
123456
telefon["Eva"] = 987654 # lägger till en nyckel och ett värde
telefon
{"Kalle": 123456, "Lisa": 454545, "Eva": 987654, "Anders": 112233}
del(telefon["Lisa"]) # ta bort element mha funktionen del()
telefon
{"Kalle": 123456, "Eva": 987654, "Anders": 112233}
telefon["Eva"] = 111111 # ändra värde på element
{"Kalle": 123456, "Eva": 111111, "Anders": 112233}

# eftersom paren inte är sorterade kan man inte använda vanlig indexering för att loopa igenom dem
# loopa igenom ett dictionary mha metoden list.items()
telefon.items() 
dict_items([("Kalle", 123456), ("Eva", 111111), ("Anders", 112233)]) # visar items i dictionary
for a, b in telefon.items():
    print (a, "tel.:", b)
Kalle tel.: 123456
Eva tel.: 111111
Anders tel.: 112233

# metoden list.keys() ger oss en lista med alla nycklar
# om vi sorterar denna lista innan vi loopar igenom den kan vi få utskrift av den strängidexerade listan sorterad på nycklarna
telefon.keys()
dict_keys(['Kalle', 'Eva', 'Anders'])
sorted(telefon.keys())
['Anders', 'Eva', 'Kalle']
for namn in sorted(telefon.keys()):
    print (namn, "=", telefon[namn])
Anders = 112233
Eva = 111111
Kalle = 123456

# metoden list.values() ger en lista av alla värden
telefon.values()
dict_values([123456, 987654, 112233])

# omvandla ett dictionary till en lista
# 1a sättet

d = {"Nils":1500, "Lisa":2300, "Kalle":2100, "Cecilia":2500, "Orjan":2400}
d
{'Nils': 1500, 'Lisa': 2300, 'Kalle': 2100, 'Cecilia': 2500, 'Orjan': 2400}
a = [(name, score) for name, score in d.items()]
a
[('Nils', 1500), ('Lisa', 2300), ('Kalle', 2100), ('Cecilia', 2500), ('Orjan', 2400)]

# fort. 1a sättet: ett MÅSTE om vi vill omvandla till en LISTA AV LISTOR
d = {"Nils":1500, "Lisa":2300, "Kalle":2100, "Cecilia":2500, "Orjan":2400}
d
{'Nils': 1500, 'Lisa': 2300, 'Kalle': 2100, 'Cecilia': 2500, 'Orjan': 2400}
a = [[name, score] for name, score in d.items()] # observera klamrar kring [name, score]
a
[['Nils', 1500], ['Lisa', 2300], ['Kalle', 2100], ['Cecilia', 2500], ['Orjan', 2400]]

# 2a sättet med funktionen list()
d = {"Nils":1500, "Lisa":2300, "Kalle":2100, "Cecilia":2500, "Orjan":2400}
d
{'Nils': 1500, 'Lisa': 2300, 'Kalle': 2100, 'Cecilia': 2500, 'Orjan': 2400}
a = list(d.items()) 
a
[('Nils', 1500), ('Lisa', 2300), ('Kalle', 2100), ('Cecilia', 2500), ('Orjan', 2400)]

# att sortera en lista av tipplar eller en lista av listor
# skapa en funktion som tar ett listelement som parameter och returnerar det värde det ska sorteras på
d = {"Nils":1500, "Lisa":2300, "Kalle":2100, "Cecilia":2500, "Orjan":2400}
d
{'Nils': 1500, 'Lisa': 2300, 'Kalle': 2100, 'Cecilia': 2500, 'Orjan': 2400}
a = [(name, score) for name, score in d.items()]
a
[('Nils', 1500), ('Lisa', 2300), ('Kalle', 2100), ('Cecilia', 2500), ('Orjan', 2400)]
a = sorted(a, key=lambda x: x[1])  # taget från geeksforgeeks.org # nyckelordet lambda används för att definiera en ANONYM funktion
print(a)                           # taget från geeksforgeeks.org
[['Nils', 1500], ['Kalle', 2100], ['Lisa', 2300], ['Orjan', 2400], ['Cecilia', 2500]] # sorterade utifrån element med index 1 vilket är score


# omvandla en lista till dictionary
d = dict(a)
d
{'Nils': 1500, 'Lisa': 2300, 'Kalle': 2100, 'Cecilia': 2500, 'Orjan': 2400}