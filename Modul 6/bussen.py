"""Hjälpkod för att komma igång
 * Notera att båda klasserna är i samma fil för att det ska underlätta.
 * Om programmet blir större bör man ha klasserna i separata filer såsom jag går genom i filmen
 * Då kan det vara läge att ställa in startvärden som jag gjort.
 * Man kan också skriva ut saker i konsollen i konstruktorn för att se att den "vaknar"
 * Denna kod hjälper mest om du siktar mot betyget E och C
 * För högre betyg krävs mer självständigt arbete
 """


class Buss:
    passagerare = []
    antal_passagerare = 0

    def run(self):  
        print("Välkommen till Buss-simulatorn")
        # Här ska menyn ligga för att göra saker
        # Vi rekommenderar switch och case här
        # Dessutom visar jag hur man anropar metoderna nedan via menyn
        # Börja nu med att köra koden för att se att det fungerar innan ni sätter igång med menyn.
        # Bygg sedan steg-för-steg och testkör koden.

    # Metoder för betyget E

    def add_passenger(self):
        # ordet pass måste finnas i "tomma" funktioner för att de ska kunna kompileras i Python, när du har 
        # något som inte är en kommentar i funktion, tex print("test") skall "pass" tas bort
        pass

        # Lägg till passagerare. Här skriver man då in ålder men eventuell annan information.
        # Om bussen är full kan inte någon passagerare stiga på

    def print_buss(self):
        # Skriv ut alla värden ur vektorn. Alltså - skriv ut alla passagerare
        pass

    def calc_total_age(self):
        # Beräkna den totala åldern. 
        # För att koden ska fungera att köra så måste denna metod justeras, alternativt att man temporärt sätter metoden med void
        pass

class Program:
    def __init__(self, *args):
        # Skapar ett objekt av klassen Buss som heter minbuss
        # Denna del av koden kan upplevas väldigt förvirrande. 
	# Men i sådana fall är det bara att "skriva av".
        minbuss = Buss()
        minbuss.run()

        # "press any key to continue" blir lite svårt i python. För att göra detta behövs antingen 
        # en specialgjord funktion eller en "Python module" som hanterar tangenttryck
        # Den enklaste lösningen har jag skrivit nedan, att trycka på enter för att komma vidare
        input("Press Enter to continue . . . ")

# Nedanstående kod är kryptisk. Om ni vill kan ni behålla de raderna.
# Följande kod aktiveras när denna python fil körs
if __name__ == "__main__":
    # skapa en instans (kopia) av klassen Program 
    my_program = Program()
