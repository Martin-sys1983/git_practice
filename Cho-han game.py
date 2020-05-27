import random

money = 100

print("_______________________________")

print("________Cho_han__game__________")
print()
def cho_han(guess, bet):
    #money can't be negative and You cant bet more than You have
    if bet <= 0:
        print("Bet should be more than 0 ")
        print("______________________________")
        return 0
    if bet > money:
        print("you don't have enough money")
        print("______________________________")
        return 0
    print(" Your guess is " + guess + "!")
    print()
    print("______Let roll that dice_______")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print("______________________________")
    print("Total amount of Your dice roll is " + str(total))
    print()

    #checking odds and eaven

    if guess.lower() == "even" and total%2 == 0:
        print("______________________________")
        print("You won  " + str(bet) + " dollars! ")
        return bet
    elif guess.lower() == "odds" and total%2 == 1:
        print("______________________________")
        print("You won  " + str(bet) + " dollars! ")
        return 0
    else:
        print()
        print("______________________________")
        print("Yo have lost " + str(bet) + " dollars!")
        return -bet
cho_han("Odds",10)
