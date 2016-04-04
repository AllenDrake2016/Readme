# name: (Zihang Huang)
# date: 2/25/2016
# description: Lab #5 -- nested loops, file input and output





#Section1
# nested loops and file output
def section1():
    print("this is section 1")

# file input
def section2():
    print("this is section 2")

section1()
section2()




# nested loops and file output
def section1():
    print("this is section 1")

    for r in range(1,8):
        for c in range(1,8):
            print(r*c,"\t",end='')
        print()

section1()




# nested loops and file output
def section1():
    print("this is section 1")

    outfile=open("table.txt","w")

    for r in range(1,8):
        for c in range(1,8):
            outfile.write(str(r*c)+"\t")
        outfile.write("\n")
    outfile.close()

section1()




# challenge #1
def challenge1():
    print("this is challenge 1")

    outfile=open("challenge1.txt","w")

    for r in range(1,41):
        for c in range(1,21):
            outfile.write(str(r*c)+"\t")
        outfile.write("\n")
    outfile.close()

challenge1()





#Section2
#file input
def section2():
    print("this is section 2")

    #open the file
    infile=open("LotsOfNumbers.txt","r")
    count=0

    #loop through all of the lines of the file
    for line in infile:
        val=int(line)
        count+=1

    #print out the number of elements
    print(count)

    #close the file
    infile.close()

section2()






#file input
def section2():
    print("this is section 2")

    #open the file
    infile=open("LotsOfNumbers.txt","r")
    count=0
    minmum=0

    #loop through all of the lines of the file
    for line in infile:
        val=int(line)
        if count==0:
            min=val
        #update the minimum value
        if val<min:
            min=val

        count+=1

    #print out  statistics
    print("number of elements:",count)
    print("minimum value:",min)


    #close the file
    infile.close()

section2()



#challenge #2
#file input
def challenge2():
    print("this is challenge 2")

    #open the file
    infile=open("LotsOfNumbers.txt","r")
    count=0
    maxmum=0

    #loop through all of the lines of the file
    for line in infile:
        val=int(line)
        if count==0:
            max=val
        #update the minimum value
        if val>max:
            max=val

        count+=1

    #print out  statistics
    print("number of elements:",count)
    print("maximum value:",max)


    #close the file
    infile.close()

challenge2()




#challenge #3
#file input
def challenge3():
    print("this is challenge 3")

    #open the file
    infile=open("LotsOfNumbers.txt","r")
    count=0
    sum=0

    #loop through all of the lines of the file
    for line in infile:
        val=int(line)
        if count==0:
            sum=val
        #update the sum value
        sum+=val

        count+=1
    average=sum/count
    #print out  statistics
    print("number of elements:",count)
    print("average value:",format(average,".2f"))


    #close the file
    infile.close()

challenge3()
