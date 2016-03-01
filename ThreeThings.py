# name: (Zihang Huang)
# date: (1/29/2016)
# description: Assignment#1 -- a demostration of input, output, and variables

name = input("Hello, what is your name?")
print("Hi", name, "your insurance payment for this month is $500.") # Change #1
payment = float(input("How much you want to pay? (the money above $500 will be paid for your next payment)")) # change #2
prepayment = payment - 500 # Change #3
print("Hello", name, "your payment has been received") # Change #4
print("Your prepay amount is $", prepayment) # Change #5
print("Thank you for choosing us!") # Change #6
