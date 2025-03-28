# generera slumptal
from random import *

# generera tom lista av lotterinummer
lottery_nums = []

# poäng för rätta bingonummer     
points = 0

# loop för att generera 10 slumpade, unika nummer
for i in range (0,10): # loop kommer ske tills vi har 10 slumpade, unika nummer
    number = randint(1,20)
    while number in lottery_nums:  # om numret redan finns i listan
        number = randint(1,20) # generera nytt nummer
    lottery_nums.append(number)

# rubrik 
print ("Spela BINGO\nDu ska nu ange tio unika tal mellan 1 och 20. Du kommer ange ett tal i taget.")

# användarens lista
chosen_nums = []
for i in range (0,10): # loop kommer ske tills vi har 10 unika nummer
    number = int(input("Ange tal {}: ".format(i+1)))
    while ((number < 1) or (number > 20) or (number in chosen_nums)):
        if ((number < 1) or (number > 20)):
            print ("Talet måste vara mellan 1-20.")
        else:
            print ("Talen måste vara unika och du har redan valt detta tal.")
        number = int(input("Ange tal {}: ".format(i+1)))
    chosen_nums.append(number)

print ("Angivna tal: {}".format(chosen_nums))
print("Slumpade tal: {}".format(lottery_nums))
for i in chosen_nums:
    if i in lottery_nums:
        print("Bingo ({})".format(i))
        points = points + 1
print ("Du fick {} poäng!".format(points))
