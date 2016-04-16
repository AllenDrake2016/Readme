# author: (Zihang Huang)
# date: 2/19/2016
# description: provide a brief description of your program
# proposed points (out of 3): 3. I believe I will get 3 for
#                             this assignment because it includes
#                             all the requirements.

def min(a,b):
    if a<b:
        return a
    else:
        return b



num1=int(input('enter a number:'))
num2=int(input('enter a number:'))

income1=(((num1+2)*8)-3)/2
income2=(((num2-2)/4)+8)*3
val=min(income1,income2)

print("income_1 is $",income1,"income_2 is $",income2)
print(val,"is the smallest income between", income1,"and",income2)

