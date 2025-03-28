# importerad modul för att kunna slumpa tal
from random import *

# rubrik
print ("Gissa talet")

# meddelande när programmet är slut
slutmeddelande = "Programmet är slut."

# slumpa fram ett tal mellan 1-100
slumpat_tal = randint (1, 100)

print ("Du ska nu gissa ett tal mellan 1 och 100.")

# gissat tal
gissat_tal = int(input("Skriv in ett tal:\n"))

# gissade talet är rätt
if gissat_tal == slumpat_tal:
    print (f"Grattis! Du gissade rätt!\n{slutmeddelande}")

# gissade talet är utanför 1-100
elif gissat_tal >= 101:
    print (f"Talet måste vara mellan 1 och 100!\n{slutmeddelande}")

# gissade talet är större än slumpade talet med 1-3
elif ((gissat_tal == (slumpat_tal + 3)) or (gissat_tal == (slumpat_tal + 2)) or (gissat_tal == (slumpat_tal + 1))):
    print (f"Ditt tal är för stort, men det var väldigt nära. Gissa på ett mindre tal!\n{slutmeddelande}")

# gissade talet är större än slumpade talet med >=4
elif gissat_tal > slumpat_tal: 
    print (f"Ditt tal är för stort. Gissa på ett mindre tal!\n{slutmeddelande}")

# gissade talet är mindre än slumpade talet med 1-3
elif ((gissat_tal == (slumpat_tal - 3)) or (gissat_tal == (slumpat_tal - 2)) or (gissat_tal == (slumpat_tal - 1))):
    print (f"Ditt tal är för litet, men det var väldigt nära. Gissa på ett större tal!\n{slutmeddelande}")

# gissade talet är mindre än slumpade talet med >=4
else: 
    print (f"Ditt tal är för litet. Gissa på ett större tal!\n{slutmeddelande}")







