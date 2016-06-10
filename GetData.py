# infile = open("RowData.txt","r")
# outfile = open("BreaksToLines.txt","w")
#
# while True:
#     word1 = infile.readline(1)
#     # print(word1)
#     if word1=="<":
#         outfile.write("\n"+word1)
#     elif not word1:
#         print("End")
#         break
#     else:
#         outfile.write(word1)
#         print(word1)
#
# infile.close()
# outfile.close()
#
# infile=open("BreaksToLines.txt","r",encoding="ascii", errors="surrogateescape")
# outfile=open("Dataout.txt","w",encoding="ascii", errors="surrogateescape")
#
#
# while True:
#     line_BTL_1=infile.readline()
#     store_line_BTL_1=line_BTL_1
#     print(store_line_BTL_1)
#     break_to_words=""
#     if len(store_line_BTL_1)>=6:
#         for n in range(6):
#             break_to_words+=store_line_BTL_1[n]
#         # print(break_to_words)
#     if not line_BTL_1:
#         print("End")
#         break
#     elif break_to_words == '<input':
#         outfile.write(store_line_BTL_1)
#
# infile.close()
# outfile.close()
#
# infile = open("Dataout.txt","r")
# outfile = open("BreaksToLines_Second_Degree.txt","w")
#
# while True:
#     word1 = infile.readline(1)
#     # print(word1)
#     if word1=='"':
#         outfile.write("\n"+word1)
#     elif not word1:
#         print("End")
#         break
#     else:
#         outfile.write(word1)
#         print(word1)
#
# infile.close()
# outfile.close()


infile=open("BreaksToLines_Second_Degree.txt","r")
outfile=open("Tidy_data_first_drgree.txt","w")

break_to_word_BTL_F_D_1="UDF"
break_to_word_BTL_F_D_2="UDF"
while True:
    line_BTL_F_D_1=infile.readline()
    store_line_BTL_F_D_1=line_BTL_F_D_1
    break_to_word_BTL_F_D_1=""
    #print(store_line_BTL_F_D_1)



    if len(store_line_BTL_F_D_1)>=8:
        for n in range(8):
            break_to_word_BTL_F_D_1+=store_line_BTL_F_D_1[n]
    #print(break_to_word_BTL_F_D_1)



    if break_to_word_BTL_F_D_1=='"rpDefen':
        outfile.write(store_line_BTL_F_D_1)
        print(store_line_BTL_F_D_1)


    elif break_to_word_BTL_F_D_2=='" value=':
        outfile.write(store_line_BTL_F_D_2)
        outfile.write(store_line_BTL_F_D_1)
        #print(store_line_BTL_F_D_1)

    elif not line_BTL_F_D_1:
        print("End")
        break

    store_line_BTL_F_D_2=line_BTL_F_D_1
    if len(line_BTL_F_D_1)>=8:
        break_to_word_BTL_F_D_2=break_to_word_BTL_F_D_1
    else:
        break_to_word_BTL_F_D_2=""


infile.close()
outfile.close()






infile=open("BreaksToLines_Second_Degree.txt","r")
outfile=open("Tidy_data_second_drgree.txt","w")

break_to_word_BTL_S_D_1="UDF"
break_to_word_BTL_S_D_2="UDF"
while True:
    line_BTL_S_D_1=infile.readline()
    store_line_BTL_S_D_1=line_BTL_S_D_1
    break_to_word_BTL_S_D_1=""
    #print(store_line_BTL_S_D_1)



    if len(store_line_BTL_S_D_1)>=8:
        for n in range(8):
            break_to_word_BTL_S_D_1+=store_line_BTL_S_D_1[n]
    #print(break_to_word_BTL_S_D_1)



    if break_to_word_BTL_S_D_1=='"rpDefen':
        #print(store_line_BTL_S_D_1)
        break_to_word_BTL_S_D_1=""
        for n in range(26):
            break_to_word_BTL_S_D_1+=store_line_BTL_S_D_1[n]
        #print(break_to_word_BTL_S_D_1)
        # if break_to_word_BTL_S_D_1=='"rpDefendantInformation_tb' or break_to_word_BTL_S_D_1=='"rpDefendantInformation$cb':
        #     outfile.write(line_BTL_S_D_1)
        #     #print(break_to_word_BTL_S_D_1)

        if break_to_word_BTL_S_D_1=='"rpDefendantInformation_tb':
            store_line_BTL_S_D_1=store_line_BTL_S_D_1.strip('"rpDefendantInformation_tb')
            outfile.write(store_line_BTL_S_D_1)
            #print(break_to_word_BTL_S_D_1)
        if break_to_word_BTL_S_D_1=='"rpDefendantInformation$cb':
            print(store_line_BTL_S_D_1)
            store_line_BTL_S_D_1=store_line_BTL_S_D_1.strip('"rpDefendantInformation$cbo')
            outfile.write(store_line_BTL_S_D_1)
            print(store_line_BTL_S_D_1)


    elif break_to_word_BTL_S_D_2=='" value=':
        outfile.write(store_line_BTL_S_D_1)
        #print(store_line_BTL_S_D_1)

    elif not line_BTL_S_D_1:
        print("End")
        break

    store_line_BTL_S_D_2=line_BTL_S_D_1
    if len(line_BTL_S_D_1)>=8:
        break_to_word_BTL_S_D_2=break_to_word_BTL_S_D_1
    else:
        break_to_word_BTL_S_D_2=""


infile.close()
outfile.close()