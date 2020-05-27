import random

money = 100

def flip_coin(guess,bet):
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

flip_coin("Heads",50)
            
    
