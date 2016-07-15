####################################################### RowData to FirstDegree
infile = open("RowData.txt","r")
outfile = open("BreakToLines_FirstDegree.txt","w")

while True:
    line_BTL_FD = infile.readline()
    words=line_BTL_FD.split()
    # print(words)
    for word in words:
        store_word=word+"\n"
        outfile.write(store_word)
    if not line_BTL_FD:
        print("End")
        break

infile.close()
outfile.close()


####################################################### FirstDegree to SecondDegree
infile=open("BreakToLines_FirstDegree.txt","r")
outfile=open("BreakToLines_SecondDegree.txt","w")

break_to_words_BTL_SD_1="UDF"
while True:
    line_BTL_SD_1=infile.readline()
    store_line_BTL_SD_1=line_BTL_SD_1
    break_to_words_BTL_SD_1=""
    #print(store_line_BTL_SD_1)

    if len(store_line_BTL_SD_1)>=24:
        for n in range(24):
            break_to_words_BTL_SD_1+=store_line_BTL_SD_1[n]
        #print(break_to_words_BTL_SD_1)
        if break_to_words_BTL_SD_1 != 'class="cptLeftAlignBold"':
            break_to_words_BTL_SD_1=""
            for n in range(8):
                break_to_words_BTL_SD_1+=store_line_BTL_SD_1[n]
            #print(break_to_words_BTL_SD_1)



    if break_to_words_BTL_SD_1 == 'class="cptLeftAlignBold"' or break_to_words_BTL_SD_1 =='onchange':
        #print(break_to_words_BTL_SD_1)
        line_BTL_SD_2=infile.readline()
        line_BTL_SD_3=infile.readline()
        outfile.write(line_BTL_SD_1)
        outfile.write(line_BTL_SD_2)
        outfile.write(line_BTL_SD_3)

    elif not line_BTL_SD_1:
        print("End")
        break
infile.close()
outfile.close()

####################################################### SecondDegree to ThirdDegree
infile=open("BreakToLines_SecondDegree.txt","r")
outfile=open("BreakToLines_ThirdDegree.txt","w")

break_to_words_BTL_TD_1="UDF"
break_to_words_BTL_TD_2="UDF"
break_to_words_BTL_TD_3="UDF"
while True:
    line_BTL_TD_1 = infile.readline()
    store_line_BTL_TD_1=line_BTL_TD_1
    break_to_words_BTL_TD_1=""

    if len(store_line_BTL_TD_1)>=8:
        for n in range(8):
            break_to_words_BTL_TD_1+=store_line_BTL_TD_1[n]
        #print(break_to_words_BTL_TD_1)


    if break_to_words_BTL_TD_1 == 'onchange':
        line_BTL_TD_2=infile.readline()
        line_BTL_TD_3=infile.readline()

        if len(line_BTL_TD_2)>=4:
            break_to_words_BTL_TD_2=""
            for n in range(4):
                break_to_words_BTL_TD_2+=line_BTL_TD_2[n]
            #print(break_to_words_BTL_TD_3)
            if break_to_words_BTL_TD_2=="type":
                line_BTL_TD_2="NA"

        if len(line_BTL_TD_3)>=4:
            break_to_words_BTL_TD_3=""
            for n in range(4):
                break_to_words_BTL_TD_3+=line_BTL_TD_3[n]
            #print(break_to_words_BTL_TD_3)
            if break_to_words_BTL_TD_3=="type":
                line_BTL_TD_3="\n"
        line_BTL_TD_2=line_BTL_TD_2.strip("\n")
        output_line=line_BTL_TD_2+","+line_BTL_TD_3
        outfile.write(output_line)

    elif len(store_line_BTL_TD_1)>=24:
        break_to_words_BTL_TD_1=""
        for n in range(24):
            break_to_words_BTL_TD_1+=store_line_BTL_TD_1[n]
        #print(break_to_words_BTL_TD_1)

        if break_to_words_BTL_TD_1=='class="cptLeftAlignBold"':
            line_BTL_TD_2=infile.readline()
            line_BTL_TD_3=infile.readline()
            line_BTL_TD_2=line_BTL_TD_2.strip("\n")
            output_line=line_BTL_TD_2+line_BTL_TD_3
            outfile.write(output_line)


    elif not line_BTL_TD_1:
        print("End")
        break

infile.close()
outfile.close()

####################################################### ThirdDegree to FourthDegree
infile=open("BreakToLines_ThirdDegree.txt","r")
outfile=open("BreakToLines_FourthDegree.txt","w")
break_to_words_D_1="UDF"
count=0
while True:
    count+=1
    line_D_1 = infile.readline()
    if count%2==0:
        for n in range(2):
            break_to_words_D_1+=line_D_1[n]
        line_D_1=line_D_1.replace("value=","")
        #print(line_D_1)
        line_D_1=line_D_1.replace('"','')
        #print(line_D_1)
        line_D_1=line_D_1.replace(',',' ')
        #print(line_D_1)
        if break_to_words_D_1=="NA":
            line_D_1=break_to_words_D_1+"\n"
        outfile.write(line_D_1)

    elif not line_D_1:
        print("End")
        break
    break_to_words_D_1=""
infile.close()
outfile.close()

####################################################### FourthDegree to Database
import csv
infile=open("BreakToLines_FourthDegree.txt","r")
rows = [line.split() for line in infile]
print(rows)
with open("Experiment.csv", "a") as outfile:
    writer = csv.writer(outfile, lineterminator=',')
    for val in rows:
        writer.writerow([val])
        print(val)
    writer = csv.writer(outfile, lineterminator='')
    writer.writerow("\n")
infile.close()