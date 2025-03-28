# rubrik
print ("Välkommen till denna pensionssimulator!")

# personens namn i bokstäver
name = str(input("Vad heter du i förnamn?\n"))

# personens ålder i siffror
age = int(input("Hur gammal är du?\n"))

# personen är 65år eller äldre
if age >= 65:
    print ("Hej "+name+". Du har redan gått i pension.\nTryck enter för att fortsätta...")

# personen är yngre än 65 år
else:
    x = (65 - age)
    print ("Hej "+name+". Du går i pension om "+str(x)+" år.\nTryck enter för att fortsätta...")