import random

global money
money = 100

number = random.randint(0,1)
def flip(guess):
    
    number = random.randint(0,1)
    if number == 0:
        number = "head"
        return number
    elif number == 1:
        number = "tails"
        return number   
        
    else:
        if number == guess :
           return "You Won"
        else:
           return "You lost"    

print(flip("head"))


