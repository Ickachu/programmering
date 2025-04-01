class Buss:
    def __init__(self):  # Initierar en Buss-klass med en lista för passagerare.
        self.passagerare = []  # Lista för att lagra passagerare
        self.antal_passagerare = 0  # Räknar antalet passagerare

    def run(self):  # Skriv ut ett välkomstmeddelande när programmet startar
        print("Välkommen till Buss-simulatorn!")

    def add_passenger(self):  # Metod för att lägga till passagerare i bussen
        while True:
            try:  # Försök att ta emot ett passagerar-ID från användaren
                passagerare_id = int(input("Ange passagerarens ID (heltal) eller ange -1 för att avsluta: "))
                if passagerare_id == -1:  # Om användaren anger -1, avsluta inmatningen
                    break
                self.passagerare.append(passagerare_id)  # Lägger till passageraren i listan
                self.antal_passagerare += 1 # Öka antalet passagerare med 1
                print(f"Passagerare {passagerare_id} har lagts till.") # Bekräftar att passageraren har lagts till
            except ValueError: # Om inmatningen inte är ett giltigt heltal... 
                print("Vänligen ange ett giltigt heltal.")  # ...skriv ut ett felmeddelande och instruera korrekt inmatning

    def print_buss(self):  # Metod för att skriva ut alla passagerare i bussen
        if not self.passagerare:  # Om det inte finns några passagerare... 
            print("Det finns inga passagerare i bussen.") # ...skriv ut meddelande till användaren
        else:  # Annars... 
            print("Passagerare i bussen:")  # ...skriv ut varje passagerare
            for passagerare in self.passagerare:
                print(passagerare)

    def calc_total_age(self):  # Metod för att beräkna den totala åldern baserat på passagerarnas ID (om de representerar åldrar)
        total_age = sum(self.passagerare)  # Beräkna summan av passagerarnas ID
        print(f"Total ålder: {total_age}")  # Skriv ut den totala åldern

class Program:
    def __init__(self):  # Initierar en instans av Buss och kör programmet
        minbuss = Buss()  # Skapar en ny Buss-instans
        minbuss.run()  # Anropar run-metoden för att skriva ut välkomstmeddelandet

        while True:
            # Skapar en meny för användaren
            print("\nMeny:")
            print("1. Lägg till passagerare")  # Alternativ för att lägga till passagerare
            print("2. Skriv ut passagerare")  # Alternativ för att skriva ut passagerare
            print("3. Beräkna total ålder")  # Alternativ för att beräkna total ålder
            print("4. Avsluta programmet")  # Alternativ för att avsluta programmet

            val = input("Välj ett alternativ (1-4): ")  # Tar emot användarens val

            if val == "1":  # Om användaren väljer alternativ 1, anropa add_passenger
                minbuss.add_passenger()
            elif val == "2":  # Om användaren väljer alternativ 2, anropa print_buss
                minbuss.print_buss()
            elif val == "3":  # Om användaren väljer alternativ 3, anropa calc_total_age
                minbuss.calc_total_age()
            elif val == "4":  # Om användaren väljer alternativ 4, avsluta programmet
                break  # Bryter loopen för att avsluta programmet
            else:# Om användaren gör ett ogiltigt val
                print("Vänligen välj ett giltigt alternativ (1-4).")

        input("Tryck Enter för att avsluta programmet... ")  # Väntar på att användaren trycker Enter innan programmet avslutas

if __name__ == "__main__":
    # Skapar en instans (kopierad objekt) av klassen Program
    my_program = Program()
