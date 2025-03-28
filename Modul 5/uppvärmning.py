# Kommentar från lärare: Koden antar att användaren alltid anger ett heltal för Fahrenheit. 
# Det kan vara bra att lägga till felhantering för att hantera scenarier där användaren anger något annat än ett heltal.
# Även om koden är ganska kort och lätt att förstå, skulle kommentarer eller förklaringar inom koden definierar korrekt en funktion
# fahr_to_cel för att konvertera temperaturer från Fahrenheit till Celsius.
# Detta är bra eftersom det separerar konverteringslogiken från huvudkoden 



celsius = 0

def fahr_to_cel(fahr):
    celsius = int(fahr - 32) * 5 / 9
    return celsius

fahr = int(input("Skriv in Fahrenheit: "))

celsius = fahr_to_cel(fahr)

print(int(celsius))