# Koden konverterar korrekt Fahrenheit till Celsius och kontrollerar om bastutemperaturen är inom det acceptabla intervallet (82-87 grader Celsius).
# Användning av funktioner gör koden lätt att läsa och underhålla. En huvudfunktion main() styr logiken.
# Kodblocket inuti try-except säkerställer att ogiltig inmatning fångas och användaren informeras.


celsius = 0 # initiera variabeln celsius


def fahr_to_cels(fahr): # funktion omvandlar fahrenheit till celsius
    celsius = int(fahr - 32) * 5 / 9 # celsius som integer
    return float(celsius) # returnerar celsius som flyttal

while True: 
    try: # testa om inmatningen är giltig
        fahr = int(input("Skriv in bastutemperatur i Fahrenheit: "))
        celsius = float(fahr_to_cels(fahr))

        if celsius < 82:
            print("Det är {} Celsius. Det är för kallt.".format(celsius))

        elif celsius > 87:
            print("Det är {} Celsius. Det är för varmt.".format(celsius))

        else: # om celsius är mellan 82-87 (celsius < 82) or (celsius > 87)
            print("Det är {} Celsius. Temperaturen är lagom.".format(celsius))
            break
    except: # om inmatningen är något annat än en integer
        print("Felaktig inmatning. Du måste skriva ett heltal.")
   
        
            


