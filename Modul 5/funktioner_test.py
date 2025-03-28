import os

from getkey import getkey, keys

def FirstChoise():

    print("Första valet")

    input("Press Enter to continue...")

 

def SecondChoise():

    print("Andra valet")

    input("Press Enter to continue...")

 

def ThirdChoise():

    print("Tredje valet")

    input("Press Enter to continue...")

 

menuOptions = ["Första", "Andra", "Tredje"]

menuSelected = 0

 

while(True):

    os.clear()

 

    if menuSelected == 0:

        print(menuOptions[0] + "<--")

        print(menuOptions[1])

        print(menuOptions[2])

    elif menuSelected == 1:

        print(menuOptions[0])

        print(menuOptions[1] + "<--")

        print(menuOptions[2])

    elif menuSelected == 2:

        print(menuOptions[0])

        print(menuOptions[1])

        print(menuOptions[2] + "<--")

 

    keyPressed = getkey()

    if keyPressed == keys.DOWN and menuSelected + 1 != len(menuOptions):

        menuSelected += 1

    elif keyPressed == keys.UP and menuSelected >= 1:

        menuSelected -=1

    elif keyPressed == keys.ENTER:

        if menuSelected == 0:

            FirstChoise()

        elif menuSelected == 1:

            SecondChoise()

        elif menuSelected == 2:

            ThirdChoise()


