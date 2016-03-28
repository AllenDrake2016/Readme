# name: (Zihang Huang)
# date: (1/29/2016)
# description: Lab#1 -- a demonstration of input,
#          mathematical operations, and formatting

name = input("Please enter your name: ")
print("Hello", name, "welcome to Lab #1.")

# more code will be entered below

cost = 5.75
print("The cost of your item is $", cost)
payment = float(input("How much will you be paying?"))
change = payment - cost
print("Your change is $", change)

# more code will be entered below
# description: convert Celsius to Fahrenheit

Celsius = float(input("Please enter the Celsius degree you want to convert: "))
Fahrenheit = (9/5)*Celsius+32
print("Fahrenheit is", Fahrenheit)

# more code will be entered below

amount_due = 5000.0
monthly_payment = amount_due/12
print("The monthly payment is", format(monthly_payment,".2f"))

# more code will be entered below

cost = float(input("How much does the object cost?"))
payment = float(input("How much you want to pay?"))
change = payment - cost
print("Your change is $", change)
