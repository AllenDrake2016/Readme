# author: Zihang Huang
# date: 2/3/2016
# description:  This program gives user a quiz about some
#               important histories of U.S.
# proposed points:  10. I believe I will get 10 for
#                   this assignment because it includes
#                   all the additional requirements.

keep_looping= True
while keep_looping == True:

    full_score=3
    # Question#1
    correct_answer1=1776
    year=float(input("The Declaration of Independence was signed in which year?(Enter number)"))
    if year==correct_answer1:
        print("Correct!")
        score=1 # User score 1 when they answer correctly
        # Correct percentage calculation
        correct_percentage=(score/full_score)*100

        # start Question #2
        correct_answer2="abraham lincoln"
        name=str(input("Who was the president died in 1865 due to the assassination?"))
        if name.lower()==correct_answer2:
            print("Correct!")
            # User score 2 when they answer correctly
            score=score+1
            correct_percentage=(score/full_score)*100

            # Question #3
            correct_answer3=2.5
            number=float(input("How many million of people were there in United States in 1776?"))
            if number==correct_answer3:
                print("Correct!")
                score=score+1
                correct_percentage=(score/full_score)*100
                print("Your final correct percentage is",format(correct_percentage,".2f"),"%")
            # User score does not get the final score
            else:
                print("Sorry, the correct answer is", correct_answer3)
                correct_percentage=(score/full_score)*100
                print("Your final correct percentage is",format(correct_percentage,".2f"),"%")
        # User does not get the second score
        else:
            print("Sorry, the correct answer is", correct_answer2)
            correct_percentage=(score/full_score)*100

            correct_answer3=2.5
            number=float(input("How many million of people were there in United States in 1776?"))
            if number==correct_answer3:
                print("Correct!")
                score=score+1
                correct_percentage=(score/full_score)*100
                print("Your final correct percentage is",format(correct_percentage,".2f"),"%")
            else:
                print("Sorry, the correct answer is", correct_answer3)
                correct_percentage=(score/full_score)*100
                print("Your final correct percentage is",format(correct_percentage,".2f"),"%")
    # User does not get the first score
    else:
        print("Sorry, the correct answer is", correct_answer1)
        score=0
        correct_percentage=(score/full_score)*100

        correct_answer2="abraham lincoln"
        name=str(input("Who was the president died in 1865 due to the assassination?"))
        if name.lower()==correct_answer2:
            print("Correct!")
            score=score+1
            correct_percentage=(score/full_score)*100

            correct_answer3=2.5
            number=float(input("How many million of people were there in United States in 1776?"))
            if number==correct_answer3:
                print("Correct!")
                score=score+1
                correct_percentage=(score/full_score)*100
                print("Your final correct percentage is",format(correct_percentage,".2f"),"%")
            else:
                print("Sorry, the correct answer is", correct_answer3)
                correct_percentage=(score/full_score)*100
                print("Your final correct percentage is",format(correct_percentage,".2f"),"%")
        else:
            print("Sorry, the correct answer is", correct_answer2)
            correct_percentage=(score/full_score)*100

            correct_answer3=2.5
            number=float(input("How many million of people were there in United States in 1776?"))
            if number==correct_answer3:
                print("Correct!")
                score=score+1
                correct_percentage=(score/full_score)*100
                print("Your final correct percentage is",format(correct_percentage,".2f"),"%")
            else:
                print("Sorry, the correct answer is", correct_answer3)
                correct_percentage=(score/full_score)*100
                print("Your final correct percentage is",format(correct_percentage,".2f"),"%")


    answer=input("Do you want to do the quiz again?")
    if answer.lower()!="yes":
        keep_looping= False
print("Thank you!")




