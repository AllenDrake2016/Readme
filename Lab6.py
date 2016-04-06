# name: (Zihang Huang)
# date: 3/24/2016
# description: Lab #6 -- lists, lists+files, lists+functions


#Sec 1
beatles=['Paul','Ringo','George','John']
print(beatles[2])


temperatures=[53.3,38.4,56.9,44.0,47.2]
sum=0
for t in temperatures:
    sum+=t
print(sum)

temperatures=[53.3,38.4,56.9,44.0,47.2]
sum=0
size=len(temperatures)
for i in range(size):
    sum+=temperatures[i]
print(sum)

# Challenge#1
numbers=[2,3,1,5,6,7,8,9]
sum=0
count=0
for t in numbers:
    count+=1
    sum+=t
average=sum/count
print(average)

numbers=[2,3,1,5,6,7,8,9]
sum=0
count=0

size=len(numbers)
for i in range(size):
    count+=1
    sum+=numbers[i]
average=sum/count
print(average)


#Sec 2 & Challange#2
infile=open('WorldSeriesWinners.txt','r')
winners=infile.readlines()
for i in range(len(winners)):
    winners[i]=winners[i].rstrip('\n')
infile.close()

team=input("Enter the name of the a team:")
if team not in winners:
    print("The",team,"have not won the World Series")
else:
    win_count=0
    for t in winners:
        if t==team:
            win_count+=1
    print("The",team,"has won the World Series",win_count,"time(s)")

#Sec 3 & Challange#3
def list_average(list):
    sum=0
    count=0
    for val in list:
        count+=1
        sum+=val
    average=sum/count
    return average
temperatures=[53.3,38.4,56.9,44.0,47.2]
avg_of_temps=list_average(temperatures)
print("the sum of temperatures is", avg_of_temps)

#Sec 4 & Challange#4
infile=open('dna.txt','r')
dna_code=infile.readlines()
for i in range(len(dna_code)):
    dna_code[i]=dna_code[i].rstrip('\n')
infile.close()

a_count=0
c_count=0
g_count=0
t_count=0

for base in dna_code:
    if base=='A':
        a_count+=1
    elif base=='C':
        c_count+=1
    elif base=='G':
        g_count+=1
    elif base=='T':
        t_count+=1

sum_of_bases=a_count+c_count+g_count+t_count
percentage_of_a=(a_count/sum_of_bases)*100
percentage_of_c=(c_count/sum_of_bases)*100
percentage_of_g=(g_count/sum_of_bases)*100
percentage_of_t=(t_count/sum_of_bases)*100

print("percentage of A's:",format(percentage_of_a,".2f"),"%")
print("percentage of C's:",format(percentage_of_c,".2f"),"%")
print("percentage of G's:",format(percentage_of_g,".2f"),"%")
print("percentage of T's:",format(percentage_of_t,".2f"),"%")
