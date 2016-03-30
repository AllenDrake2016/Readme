# name: (Zihang Huang)
# date: 2/5/2016
# description: Lab #2 -- logical operators, boolean variables, and while loops

# in all lower case
# print("Welcome to Lab #2!")
# answer=input("Are you ready to get started?")
# if answer == "yes":
#     print("Excellent! Here we go...")
# else:
#     print("um... we'll let's get started anyways...")
# respones=input("Enter some text: ")
# print("Your text in all lower case: ", respones.lower())
#
# # Modified code
# print("Welcome to Lab #2!")
# answer=input("Are you ready to get started?")
# if answer.lower() == "yes":
#     print("Excellent! Here we go...")
# else:
#     print("um... we'll let's get started anyways...")
#
# # And
# temperature=int(input("Enter a number"))
# if 68<temperature and temperature<74:
#     print("Within range")
# else:
#     print("Not within range")
#
# # Challenge #2
# print("Welcome to our cinema")
# age=int(input("Please enter your age to check your price you ought to pay."))
# if age>=13 and age<=65:
#     print("You should pay full price")
# else:
#     print("You have the right to have discount")
#
# # Sec 3.2 "Or"
# print("Welcome to Lab #2!")
# answer=input("Are you ready to get started?")
# if answer.lower() == "yes" or answer.lower()=="ok" or answer.lower()=="yeah":
#     print("Excellent! Here we go...")
# else:
#     print("um... we'll let's get started anyways...")

# # Sec 5
# val=0
# while val<10:
#     print(val)
#     val=val+2

# challenge #4
# val=0
# while val<=70:
#     print(val)
#     val=val+7
#

# Sec 6 loops
keep_looping= True
count=0
while keep_looping == True:
    print("So far, you've looped", count,"time(s)")
    answer=input("Do you want to loop again?")
    if answer.lower()=="yes":
        count = count+1
    else:
        keep_looping= False
print("You looped", count, "time(s)")

# challenge #5
keep_looping=True
count=0
while keep_looping == True:
    answer=input("Do you want to loop again?")
    if answer.lower()=="yes" or answer.lower()=="ok":
        count = count+1
    else:
        keep_looping= False
print("You have said ""yes"" or ""ok""", count, "time(s)")

# Assignment #3
full_score=3
# Question#1
correct_answer1=1776
year=float(input("The Declaration of Independence was signed in which year?(Enter number)"))
if year==correct_answer1:
    print("Correct!")
    score=1 # User score 1 when they answer correctly
    # Correct percentage calculation
    correct_percentage=(score/full_score)*100
    print("Correct percentage",format(correct_percentage,".2f"),"%")
    # start Question #2
    correct_answer2="Abraham Lincoln"
    name=str(input("Who was the president died in 1865 due to the assassination?"))
    if name==correct_answer2:
        print("Correct!")
        # User score 2 when they answer correctly
        score=score+1
        correct_percentage=(score/full_score)*100
        print("Correct percentage:",format(correct_percentage,".2f"),"%")
        # Question #3
        correct_answer3=2.5
        number=float(input("How many million of people were there in United States in 1776"))
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
        print("Correct percentage:",format(correct_percentage,".2f"),"%")
        correct_answer3=2.5
        number=float(input("How many million of people were there in United States in 1776"))
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
    print("Correct percentage",format(correct_percentage,".2f"),"%")
    correct_answer2="Abraham Lincoln"
    name=str(input("Who was the president died in 1865 due to the assassination?"))
    if name==correct_answer2:
        print("Correct!")
        score=score+1
        correct_percentage=(score/full_score)*100
        print("Correct percentage:",format(correct_percentage,".2f"),"%")
        correct_answer3=2.5
        number=float(input("How many million of people were there in United States in 1776"))
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
        print("Correct percentage:",format(correct_percentage,".2f"),"%")
        correct_answer3=2.5
        number=float(input("How many million of people were there in United States in 1776"))
        if number==correct_answer3:
            print("Correct!")
            score=score+1
            correct_percentage=(score/full_score)*100
            print("Your final correct percentage is",format(correct_percentage,".2f"),"%")
        else:
            print("Sorry, the correct answer is", correct_answer3)
            correct_percentage=(score/full_score)*100
            print("Your final correct percentage is",format(correct_percentage,".2f"),"%")
