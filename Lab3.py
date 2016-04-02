# name: (Zihang Huang)
# date: (2/12/2016)
# description: Lab3; loops, nested loops, and accumulators




# for num in [1,2,3,4,5,6]:
#     print(num)
# for i in range(7):
#     print("hello")
#
# # count
#
# count=4
# for i in range(count):
#     print("Lab is awesome")
#
# count=int(input("Enter a number"))
# for i in range(count):
#     print("welcome to lab 3")
#






# # Sec 3
# for num in range(5):
#     val=int(input("enter a number"))
#     if num==0:
#         min=val
#     elif val<min:
#         min=val
# print("min number you choose is", min)






# # challenge #2
# for num in range(5):
#     val=int(input("enter a number"))
#     if num==0:
#         min=val
#         max=val
#     elif val<min:
#         min=val
#     elif val>max:
#         max=val
# print("min number you choose is", min, "max number", max)






# # Sec 4 "Running Total"
#
# total=0
# for num in range(5):
#     val=int(input("enter a number"))
#     total+=val
# print("Sum equal", total)







# # challenge #3
#
# total=0
# for num in range(5):
#     val=int(input("enter a number"))
#     total+=val
# average=total/5
# print("Average equal", average)






# # challenge #4
#
# total=0
# for num in range(101):
#     val=int(num)
#     total+=val
# print("Sum equal", total)







## Sec #5 Nested loops
#
# # only c
# for c in range(10):
#     print(c,end='')






# # three times c
# for r in range(3):
#     for c in range(10):
#         print(c,end='')




#
# # 2 dimension
# for r in range(3):
#     for c in range(10):
#         print(c,end='')
#     print()
#
#







# # challenge #5
#
# for r in range(5):
#     for c in range(7):
#         print(r+1,end='')
#     print()



# only c
battleship_location=int(input("Where do you want to put your battleship?"))
for c in range(10):
    if battleship_location==c:
        print("X",end='')
    else:
        print("O", end='')



# # Sec 3
# for num in range(5):
#     val=int(input("enter a number"))
#     if num==0:
#         min=val
#     elif val<min:
#         min=val
# print("min number you choose is", min)
