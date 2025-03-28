import os

from getkey import getkey, keys

def FirstChoice():
    print("Första valet")
    input("Press Enter to continue...")

def SecondChoice():
    print("Andra valet")
    input("Press Enter to continue...")

def ThirdChoice():
    print("Tredje valet")
    input("Press Enter to continue...")

def EndProgram():
    print("Avslutar programmet")
    input("Press Enter to continue...")


menuOptions = ["Första", "Andra", "Tredje", "Avsluta"]
menuSelected = 0


while(True):
    os.system("cls||clear")
    print("\x1b[?25l")

    if menuSelected == 0:
        print(menuOptions[0] + " <--")
        print(menuOptions[1])
        print(menuOptions[2])
        print(menuOptions[3])
    elif menuSelected == 1:
        print(menuOptions[0])
        print(menuOptions[1] + " <--")
        print(menuOptions[2])
        print(menuOptions[3])
    elif menuSelected == 2:
        print(menuOptions[0])
        print(menuOptions[1])
        print(menuOptions[2] + " <--")
        print(menuOptions[3])
    elif menuSelected == 3:
        print(menuOptions[0])
        print(menuOptions[1])
        print(menuOptions[2])
        print(menuOptions[3] + " <--")
        
    keyPressed = getkey()
    print("Key pressed: " + keyPressed)
    if keyPressed == keys.S and menuSelected + 1 != len(menuOptions):
        menuSelected += 1
        print("tryckt ner")
    elif keyPressed == keys.W and not (menuSelected == 0):
        menuSelected -= 1
        print("tryckt upp")
    elif keyPressed == keys.ENTER:
        print("tryckt enter")
        if menuSelected == 0:
            FirstChoice()
        elif menuSelected == 1:
            SecondChoice()
        elif menuSelected == 2:
            ThirdChoice()
        elif menuSelected == 3:
            EndProgram()
            print("\x1b[?25h]")

