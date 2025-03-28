# välkomnande rubrik
print ("Välkommen till denna pensionssimulator!")

# personen anger sitt namn i bokstäver
name = str(input("Vad heter du i förnamn? "))

# personen anger sin ålder i siffror
age = int(input("Hur gammal är du? "))

# dpa desired pension age / önskad pensionsålder
dpa = int(input("Vid vilken ålder vill du gå i pension? "))

x = (dpa - age)
print ("Hej "+name+". Du går i pension om "+str(x)+" år.")
print ("Tryck enter för att fortsätta...")