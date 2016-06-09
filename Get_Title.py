infile=open("BreaksToLines_Second_Degree.txt","r")
outfile=open("Title_Raw.txt","w")

break_to_word_Title_R_1="UDF"
break_to_word_Title_R_2="UDF"
while True:
    line_Title_R_1=infile.readline()
    store_line_Title_R_1=line_Title_R_1
    break_to_word_Title_R_1=""
    #print(store_line_Title_R_1)



    if len(store_line_Title_R_1)>=8:
        for n in range(8):
            break_to_word_Title_R_1+=store_line_Title_R_1[n]
    #print(break_to_word_Title_R_1)



    if break_to_word_Title_R_1=='"rpDefen':
        #print(store_line_Title_R_1)
        break_to_word_Title_R_1=""
        for n in range(26):
            break_to_word_Title_R_1+=store_line_Title_R_1[n]
        #print(break_to_word_Title_R_1)
        # if break_to_word_Title_R_1=='"rpDefendantInformation_tb' or break_to_word_Title_R_1=='"rpDefendantInformation$cb':
        #     outfile.write(line_Title_R_1)
        #     #print(break_to_word_Title_R_1)

        if break_to_word_Title_R_1=='"rpDefendantInformation_tb':
            store_line_Title_R_1=store_line_Title_R_1.strip('"rpDefendantInformation_tb')
            outfile.write(store_line_Title_R_1)
            #print(break_to_word_Title_R_1)
        if break_to_word_Title_R_1=='"rpDefendantInformation$cb':
            print(store_line_Title_R_1)
            store_line_Title_R_1=store_line_Title_R_1.strip('"rpDefendantInformation$cbo')
            outfile.write(store_line_Title_R_1)
            print(store_line_Title_R_1)


    # elif break_to_word_Title_R_2=='" value=':
    #     outfile.write(store_line_Title_R_1)
    #     #print(store_line_Title_R_1)

    elif not line_Title_R_1:
        print("End")
        break

    store_line_Title_R_2=line_Title_R_1
    if len(line_Title_R_1)>=8:
        break_to_word_Title_R_2=break_to_word_Title_R_1
    else:
        break_to_word_Title_R_2=""




infile.close()
outfile.close()

infile=open("Title_Raw.txt","r")
outfile=open("Title.txt","w")

outfile_line=""
while True:
    line_Title_1=infile.readline()
    store_line_Title_1=line_Title_1.strip("\n")
    store_line_Title_1=store_line_Title_1+"\t"
    outfile_line+=store_line_Title_1

    if not line_Title_1:
        outfile_line=outfile_line.strip("\t")+"\n"
        print("End")
        break
outfile.write(outfile_line)

infile.close()
outfile.close()

infile=open("Title.txt","r")
outfile=open("Database.txt","a")
line_Data_1=infile.readline()
outfile.write(line_Data_1)
infile.close()
outfile.close()