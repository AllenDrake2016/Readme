# author: (Zihang Huang)
# date: 2/12/2016
# description: This program gives user a battleship game
# proposed points (out of 20): 18. I believe I will get 18 for
#                              this assignment because, beside two-dimension,
#                              it include all the additional requirements.


print("Please design the size of the battleship board to be play!")
size=int(input("How big the size do you want to have?(Choose a positive integer)"))
print("Good! You have made your battleship board!")



choice=str(input("Would you like to choose the battleship location (Yes or No)?"))
count=0
if choice.lower()=="yes":
    print("Now, input a integer between 0 and", size)
    battleship_location=int(input("Where do you want to put your battleship? (Please input a integer)"))
    for c in range(size+1):
        if battleship_location==c:
            print("X",end='')
        else:
            print("O", end='')
    print()

    keep_looping= True
    while keep_looping == True and count<5:
        count+=1
        print("Please input a integer between 0 and", size)
        attack_location=(int(input("Guess the location of the battleship")))
        if attack_location==battleship_location:

            for c in range(size+1):
                if battleship_location==c:
                    print("!",end='')
                else:
                    print("O", end='')
            print()

            print("You sank my battleship!")
            keep_looping=False
        elif -5<attack_location-battleship_location<-1 or 1<attack_location-battleship_location<5:

            for c in range(size+1):
                if battleship_location==c:
                    print("X",end='')
                elif attack_location==c:
                    print("@",end='')
                else:
                    print("O", end='')
            print()

            print("You miss, but close. Try again")
        elif attack_location-battleship_location==-1 or attack_location-battleship_location==1:

            for c in range(size+1):
                if battleship_location==c:
                    print("X",end='')
                elif attack_location==c:
                    print("@",end='')
                else:
                    print("O", end='')
            print()

            print("You are so close to the target, I am sure you won't miss it next time!")
        else:
            for c in range(size+1):
                if battleship_location==c:
                    print("X",end='')
                elif attack_location==c:
                    print("@",end='')
                else:
                    print("O", end='')
            print()

            print("Sorry, that's not even close. Please try again")
    if keep_looping!=True:
        print("The total number of missiles you fire is", count)
    else:
        print("Sorry captain, we are out of missiles, GAME OVER!")

else:
    print("Ok, the location will be chosen randamly by us.")
    # if user choose no, he or she will be shown location will be chosen randamly.
    import random
    battleship_location=random.randint(0,size)
    for c in range(size+1):
        if battleship_location==c:
            print("X",end='')
        else:
            print("O", end='')
    print()

    keep_looping= True
    while keep_looping == True and count<5:
        count+=1
        print("Please input a integer between 0 and", size)
        attack_location=(int(input("Guess the location of the battleship")))
        if attack_location==battleship_location:

            for c in range(size+1):
                if battleship_location==c:
                    print("!",end='')
                else:
                    print("O", end='')
            print()

            print("You sank my battleship!")
            keep_looping=False
        elif -5<attack_location-battleship_location<-1 or 1<attack_location-battleship_location<5:

            for c in range(size+1):
                if battleship_location==c:
                    print("X",end='')
                elif attack_location==c:
                    print("@",end='')
                else:
                    print("O", end='')
            print()

            print("You miss, but close. Try again")
        elif attack_location-battleship_location==-1 or attack_location-battleship_location==1:

            for c in range(size+1):
                if battleship_location==c:
                    print("X",end='')
                elif attack_location==c:
                    print("@",end='')
                else:
                    print("O", end='')
            print()

            print("You are so close to the target, I am sure you won't miss it next time!")
        else:
            for c in range(size+1):
                if battleship_location==c:
                    print("X",end='')
                elif attack_location==c:
                    print("@",end='')
                else:
                    print("O", end='')
            print()


            print("Sorry, that's not even close. Please try again")
    if keep_looping!=True:
        print("The total number of missiles you fire is", count)
    else:
        print("Sorry captain, we are out of missiles, GAME OVER!")



