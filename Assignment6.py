# author: (Zihang Huang)
# date: 2/12/2016
# description: This program gives user a dice game, pig
# proposed points (out of 10): 10. I think I might get 10 for
#                              this assignment because,
#                              it include all the additional requirements.




import random


# a value-returning function returns a random
def roll_die(X):
    result=random.randint(1,X)
    return result

# main function contains the code to play the game
def print_menu():
    print("press r to (r)oll.")
    print("press h to (h)old.")
    print("press d for a (d)escription of the rules")
    print("press q to (q)uit")
    print()


# a function contains the descriptions
def print_rule():
    print("Pig is a dice game with simple rules:")
    print("The goal is to reach a certain number of pointsin the fewest number of turns.")
    print("A player repeatedly rolls a die until either a 1 'pig'")
    print("is rolled or the player holds and scores the sum of the rolls.")
    print("At any time during a player's turn, the player is faced with two decisions:")
    print("roll:")
    print("1:If the player rolls a '1', the player scores nothing; the turn total is set to 0; and the number of")
    print("turns is increased")
    print("2 - 6: the number is added to the player's turn total.")
    print("hold:")
    print("The turn total is added to the player's score and the number of turns is increased")
    print()

# main function contains codes to play the game
def main():
    turns=0
    score=0
    turn_total=0
    # limit of the score
    limit=a
    # sides on the die
    sides=b
    roll_die(sides)
    keep_looping=True
    while keep_looping==True and score<limit:
        respond=str(input("What do you want to do? (press m for menu):"))
        if respond=="m":
            print_menu()
        elif respond=="r":
            roll=roll_die(X=sides)
            if roll==1:
                turn_total=0
                turns+=1
            else:
                turn_total+=roll
        elif respond=="h":
            score+=turn_total
            turn_total=0
            turns+=1
        elif respond=="d":
            print_rule()
        elif respond=="q":
            keep_looping=False
        print("You took",turns,"turns")
        print("You have",score,"points")
        print("Your current total is:",turn_total)
        print()
    if keep_looping==False:
        print("Game Over")
    else:
        print("Game Over")

print("Hi, welcome to Pig!")
a=int(input("What score would you like to play?"))
b=int(input("How many sides on the die?"))
main()

