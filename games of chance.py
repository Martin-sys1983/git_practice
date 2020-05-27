import random

money = 100

def coin_flip(guess,bet):
    global money
    #intro 
    print("_________________________________")
    print("You are playing 'Heads and Tails' ")
    print("_________________________________")

    
    #code is checking if bet is less than You have in your pool
    if bet > money:
        print("_________________________________")
        print("You cannot bet more than you have!")
        return 0
        print("_________________________________")
    
    elif bet < 0:
        print(" You need to use positive money:)")

    # code prints result pf the coin flip
    else:
        number = random.randint(0,1)
        if number == 0:
            result = "heads"
        else:
            result = "tails"

        print("You flipped a " + result + " !")
     #lose or won conditions with lower methof
        if guess.lower() == result.lower():
            money+=bet
            print("You won " + str(bet) + " $ ")
            print("Your current pool of money is " + str(money) + " $")
            print("_________________________________")
            return bet
        else:
            money-=bet
            print("You have lost " + str(bet) + " $! ")
            print ("Your current pool is " + str(money) + " $")
            print("_________________________________")
            return -bet




def cho_han(guess, bet):
    #money can't be negative and You cant bet more than You have
    print("_______________________________")

    print("________Cho_han__game__________")
    print()
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



def higher_card(bet):
    print("__________________________________")
    print()
    print("__________Pick_Higher_Card________")

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
        return -bet
    else:
        print("it was a Tie!!!!")
        print()
        print("__________________________________")
        return 0


def roulette(guess, bet):
    #First we check if money we are betting are bigger then nothing
    if bet <= 0:
        print("---------------------------")
        print()
        print("You need bet more than zero")
        return 0
    print("---------------------------")
    print()

    #wheel has 36 numbers plus one more which is 00 so we gona use 37 numbers
    print("---------------------------")
    print()
    print("      Let's Play         ")
    
    result = random.randint(0, 37)
    if result == 37 :
        print(" The wheel landed on 00 ")
    else:
        print("The wheel landed on " + str(result) )

    #we gonna czeck if we guess the outcome
    if guess == "even" and result % 2 == 0 and result != 0:
        print(str(result) + " is an even number.")
        print()
        print("You won " + str(bet) + " dollars!")
        print()
        print("---------------------------")
        return bet
    
    elif guess == "odd" and result % 2 == 1 and result != 37:
        print(str(result) + " is an odd number.")
        print()
        print("You won " + str(bet) + " dollars!")
        print()
        print("---------------------------")
        return bet
    elif guess == result:
        print("You guessed " + str(guess) + " and the result was " + str(result))
        print("You won " + str(bet * 35)+" dollars!")
        print("------------------")
        return bet * 35
    else:
        print("You lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet

money += coin_flip("Heads", 10)
money += cho_han("Even", 2)
money += higher_card(7)
money += roulette("Even", 10)
money += roulette(3, 1)
money += roulette("odd", money)
print("Your total amount of money is " + str(money))     
        
        
        
    
    
