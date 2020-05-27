import random

money = 100

print("__________________________________")
print()
print("__________Pick_Higher_Card________")

def higher_card(bet):
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        print("------------------")
        return 0
    #draw a card from the 10 cards and print results
    print("__________________________________")
    print()
    print("____________Let's_play____________")
    print()

    mine_pick = random.randint(1, 10)
    computer_pick = random.randint(1, 10)

    print("__________________________________")
    print("I pick upa a " + str(mine_pick) + " points card!")
    print()
    print("Computer pick up a " + str(computer_pick) + " points card!")

    #now let's check who pick up a higher card
    if mine_pick > computer_pick :
        print()
        print("I won!!! " + str(bet) + " dollars")
        print("__________________________________")
        return bet
    elif mine_pick < computer_pick :
        print("Computer won and I lost!!! " + str(bet) + " dollars")
        print()
        print("__________________________________")
    else:
        print("it was a Tie!!!!")
        print()
        print("__________________________________")
        return 0
higher_card(30)
        
