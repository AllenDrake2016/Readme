# name: (Zihang Huang)
# date: (2/19/2016)
# description: Lab4; void functions, parameters, arguments, and value-returning functions





# # Sec 2
# def main():
#     print("Hello")
#     message()
#     print("Goodbye")
#
# def message():
#     print("It is warm outside!")
#
# main()
#
#
#
# # Challenge #1
# def main():
#     print("Hello")
#     message()
#     print("Goodbye")
#
# def message():
#     for c in range(5):
#         print("It is warm outside!")
#
# main()
#
#
#
# # Sec #3
# def vote_verification(age):
#     if age>=18:
#         print("You can vote!")
#     else:
#         print("You can't now!")
#
# val= int(input("How old are you?"))
# vote_verification(val)
#
#
# # Challenge #2
#
# def graduating_senior(credit):
#     if credit>=124:
#         print("You can graduate")
#     else:
#         print("You need to take more classes")
#     credit_to_graduate=124-credit
#     print("You have",credit,"credits. You still have",credit_to_graduate,"to go")
#
# credit=int(input("What is your credits?"))
# graduating_senior(credit)



# # Sec 4 and challenge #3
# def which_is_least(first, second):
#     if first<second:
#         print("first is least")
#     else:
#         print("second is least")
#
#
# a=int(input('enter a number:'))
# b=int(input('enter another number:'))
# which_is_least(a,b)


# # Sec 5
# def sum(num1, num2):
#     result=num1+num2
#     return result
#
# val=sum(2,3)
# print(val)
#
# # challenge #4
# def power(num1,num2):
#     result=num1**num2
#     return result
# val=power(4,3)
# print(val)







# # Sec 6
#
# def min(a,b):
#     if a<b:
#         return a
#     else:
#         return b
# num1=int(input('enter a number:'))
# num2=int(input('enter a number:'))
# val=min(num1,num2)
# print(val,"is the smallest number between", num1,"and",num2)




# challenge #5
def max(a,b):
    if a>b:
        return a
    else:
        return b

num1=int(input('enter a number:'))
num2=int(input('enter a number:'))
val=min(num1,num2)
print(val,"is the smallest number between", num1,"and",num2)
