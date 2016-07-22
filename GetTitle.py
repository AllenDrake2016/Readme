infile=open("BreakToLines_SecondDegree.txt","r")
outfile=open("Title.txt","w")

break_to_words_T_1="UDF"

while True:
    line_BTL_T_1 = infile.readline()
    store_line_T_1=line_BTL_T_1
    break_to_words_T_1=""

    if len(store_line_T_1)>=24:
        for n in range(24):
            break_to_words_T_1+=store_line_T_1[n]
        #print(break_to_words_T_1)

    if break_to_words_T_1 == 'class="cptLeftAlignBold"':
        line_BTL_T_2=infile.readline()
        line_BTL_T_3=infile.readline()
        line_BTL_T_2=line_BTL_T_2.strip("\n")
        output_line=line_BTL_T_2+line_BTL_T_3
        outfile.write(output_line)


    if not line_BTL_T_1:
        print("End")
        break

infile.close()
outfile.close()


import csv
infile=open("Title.txt","r")
rows = [line.split() for line in infile]
with open("Experiment.csv", "a") as outfile:
    writer = csv.writer(outfile, lineterminator=',')
    for val in rows:
        writer.writerow([val])
    writer = csv.writer(outfile, lineterminator='')
    writer.writerow("\n")
infile.close()