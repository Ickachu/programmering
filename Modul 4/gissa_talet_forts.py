# importerad modul för att kunna slumpa tal
from random import *

# slumpa fram ett tal mellan 1-100
rand_num = randint (1, 100)
# print (rand_num) # för att testa program

# antal gissningar. startpunkt är 1, då första gissningen kan vara rätt vilket skulle innebära att while-loopen inte sker
no_of_guesses = 1

# maximalt antal gissningar innan spelet avslutas
max_guesses = 10

# meddelande när spelet är slut
end_msg = "Spelet är slut."

# rubrik 
print ("Gissa talet\nDu ska nu gissa ett tal mellan 1 och 100.")

# gissat tal
guess_num = int(input("Skriv in ett tal: "))

# gissa tal 
while guess_num != rand_num:
    # gissade talet är utanför spannet 1-100
    if ((guess_num >= 101) or (guess_num <= 0)):
        print ("Ditt tal är ogiltigt. Gissa på ett tal mellan 1-100!")
    # gissade talet är större än slumpade talet med 1-3
    elif ((guess_num == (rand_num + 3)) or (guess_num == (rand_num + 2)) or (guess_num == (rand_num + 1))):
        print ("Ditt tal är för stort, men det var väldigt nära. Gissa på ett mindre tal!")
    # gissade talet är större än slumpade talet med >=4
    elif guess_num > rand_num: 
        print ("Ditt tal är för stort. Gissa på ett mindre tal!")
    # gissade talet är mindre än slumpade talet med 1-3
    elif ((guess_num == (rand_num - 3)) or (guess_num == (rand_num - 2)) or (guess_num == (rand_num - 1))):
        print ("Ditt tal är för litet, men det var väldigt nära. Gissa på ett större tal!")
    # gissade talet är mindre än slumpade talet med >=4
    else: 
        print ("Ditt tal är för litet. Gissa på ett större tal!")

    guess_num = int(input("Skriv in ett tal: "))
    # öka antal gissningar med 1
    no_of_guesses = no_of_guesses + 1
    # om max antal gissningar uppnåtts: bryt
    if no_of_guesses == max_guesses:
        break

# om gissat tal är samma som slumpat tal
if guess_num == rand_num:
    print ("Grattis! Du gissade rätt! Du behövde {} gissningar på dig.".format(no_of_guesses))
# i andra fall
else:
    print ("Du gissade fel. Du har använt alla {} gissningar.".format(max_guesses))

print (end_msg)
