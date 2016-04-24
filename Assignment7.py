# author: (Zihang Huang)
# date: 3/3/2016
# description: This program designed to show user the hidden message
#              behind an art, which is call steganography.
# proposed points (out of 20): 20. I think I might get 10 for
#                              this assignment because,
#                              it include all the additional requirements.


#pring menu function
def print_menu():
    print("press 1 for red steganography")
    print("press 2 for green steganography")
    print("press 3 for blue steganography")
    print("press 4 for grayscale")
    print("press 5 for border")



def red_steganography():
    infile = open("StarryNight.ppm","r")
    outfile = open("out.ppm","w")

    #read in 1st 4 lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    #write out to output file
    outfile.write(line1)
    outfile.write(line2)
    outfile.write(line3)
    outfile.write(line4)

    # Use nested loop to process the image
    count=0
    while count<400*317:
        count+=1

        red = int(infile.readline())
        green = int(infile.readline())
        blue = int(infile.readline())


        if red%2 == 0:   #even
            r = 0
            g = 0
            b = 0
        else:
            r = 255
            g = 255
            b = 255

        outfile.write(str(r) + "\n")
        outfile.write(str(g) + "\n")
        outfile.write(str(b) + "\n")

    infile.close()
    outfile.close()


def green_steganography():
    infile = open("StarryNight.ppm","r")
    outfile = open("out.ppm","w")

    #read in 1st 4 lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    #write out to output file
    outfile.write(line1)
    outfile.write(line2)
    outfile.write(line3)
    outfile.write(line4)

    #process all of the pixels
    for i in range(400*317):
        red = int(infile.readline())
        green = int(infile.readline())
        blue = int(infile.readline())


        if green%2 == 0:   #even
            r = 0
            g = 0
            b = 0
        else:
            r = 255
            g = 255
            b = 255

        outfile.write(str(r) + "\n")
        outfile.write(str(g) + "\n")
        outfile.write(str(b) + "\n")

    infile.close()
    outfile.close()


def blue_steganography():
    infile = open("StarryNight.ppm","r")
    outfile = open("out.ppm","w")

    #read in 1st 4 lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    #write out to output file
    outfile.write(line1)
    outfile.write(line2)
    outfile.write(line3)
    outfile.write(line4)

    #process all of the pixels
    for i in range(400*317):
        red = int(infile.readline())
        green = int(infile.readline())
        blue = int(infile.readline())


        if blue%2 == 0:   #even
            r = 0
            g = 0
            b = 0
        else:
            r = 255
            g = 255
            b = 255

        outfile.write(str(r) + "\n")
        outfile.write(str(g) + "\n")
        outfile.write(str(b) + "\n")

    infile.close()
    outfile.close()



def gray_scale():
    infile = open("StarryNight.ppm",'r')
    outfile = open("out.ppm",'w')

    #read in put file first 4 lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    #write 1st four lines to output file
    outfile.write(line1)
    outfile.write(line2)
    outfile.write(line3)
    outfile.write(line4)


    for i in range(400*317):

        red=int(infile.readline())
        green=int(infile.readline())
        blue=int(infile.readline())
        avg = (red + green+ blue) // 3

        r=avg
        g=avg
        b=avg

        outfile.write(str(r)+"\n")
        outfile.write(str(g)+"\n")
        outfile.write(str(b)+"\n")
    infile.close()
    outfile.close()


def boarder():
    infile = open("StarryNight.ppm",'r')
    outfile = open("out.ppm",'w')

    #read in put file first 4 lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    #write 1st four lines to output file
    outfile.write(line1)
    outfile.write(line2)
    outfile.write(line3)
    outfile.write(line4)

    for row in range(317):
        for col in range(400):

            red=int(infile.readline())
            green=int(infile.readline())
            blue=int(infile.readline())
            if row<10 or col<10:
                r=0
                g=0
                b=255
            elif row>307 or col>390:
                r=0
                g=0
                b=255

            else:
                r=red
                g=green
                b=blue
            outfile.write(str(r)+"\n")
            outfile.write(str(g)+"\n")
            outfile.write(str(b)+"\n")
    infile.close()
    outfile.close()


def main():
    print_menu()
    choice=int(input("What is your choice?"))
    if choice==1:
        red_steganography()
    elif choice==2:
        green_steganography()
    elif choice==3:
        blue_steganography()
    elif choice==4:
        gray_scale()
    elif choice==5:
        boarder()
    infile = open("StarryNight.ppm",'r')

    #read in put file first 4 lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    sum_r=0
    sum_g=0
    sum_b=0
    count=0
    for i in range(400*317):
        count+=1
        red=int(infile.readline())
        green=int(infile.readline())
        blue=int(infile.readline())
        sum_r += red
        sum_g += green
        sum_b += blue

        r_avg = sum_r/count
        g_avg = sum_g/count
        b_avg = sum_b/count


    infile.close()

    print("red average:",format(r_avg,".2f"))
    print("green average:",format(g_avg,".2f"))
    print("blue average:",format(b_avg,".2f"))




main()