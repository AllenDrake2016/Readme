infile=open("Tidy_data_first_drgree.txt","r")
outfile=open("Defendant_Infomation.txt","w")

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



    # if break_to_word_BTL_F_D_1=='"rpDefen':
    #     #print(store_line_BTL_F_D_1)
    #     break_to_word_BTL_F_D_1=""
    #     for n in range(26):
    #         break_to_word_BTL_F_D_1+=store_line_BTL_F_D_1[n]
    #     print(break_to_word_BTL_F_D_1)
    #     if break_to_word_BTL_F_D_1=='"rpDefendantInformation_tb' or break_to_word_BTL_F_D_1=='"rpDefendantInformation$cb':
    #         outfile.write(line_BTL_F_D_1)
    #         #print(break_to_word_BTL_F_D_1)
    #
    #     if break_to_word_BTL_F_D_1=='"rpDefendantInformation_tb':
    #         store_line_BTL_F_D_1=store_line_BTL_F_D_1.strip('"rpDefendantInformation_tb')
    #         outfile.write(store_line_BTL_F_D_1)
    #         #print(break_to_word_BTL_F_D_1)
    #     if break_to_word_BTL_F_D_1=='"rpDefendantInformation$cb':
    #         print(store_line_BTL_F_D_1)
    #         store_line_BTL_F_D_1=store_line_BTL_F_D_1.strip('"rpDefendantInformation$cbo')
    #         outfile.write(store_line_BTL_F_D_1)
    #         print(store_line_BTL_F_D_1)
    #
    #
    if break_to_word_BTL_F_D_2=='" value=':
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


infile=open("Defendant_Infomation.txt","r")
outfile=open("Database.txt","a")

rows = [line.split() for line in infile]
#print(rows)
outfile.write(str(rows))

infile.close()
outfile.close()