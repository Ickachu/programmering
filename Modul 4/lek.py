pokerhand = [
    [1, 5],
    [6, 9],
    [1, 8]
]

common = [1, 4, 5, 7, 3]

pair = 0

for hand in pokerhand:
  #  print (hand)
    for card in hand:
    #    print (card)
        if card in common:
   #         print ("If statement true")
            pair = pair + 1
  #          print (str(pair))
    print ("You have " + str(pair) + " pairs")
    print ("Your hand" + str(hand))
    pair = 0
        
   #         print ("You have a pair")
     #       print (hand)