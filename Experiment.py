####################################################### Strip and replace method (Remove)
# value = '"50342=Data,231"'
#
# # Strip all digits.
# # ... Also remove equals sign and comma.
# result = value.strip(',')
# print(result.replace("342",""))
#
#
#
# print(sys.argv[0])
# print(sys.argv)

####################################################### sys
# import sys
#
# infile = open(sys.argv[0], 'r')
# outfile=open("Experiment.txt",'w')
#
# while True:
#     line_BTL_T_1 = infile.readline()
#     outfile.write(line_BTL_T_1)
#     if not line_BTL_T_1:
#         print("End")
#         break
#
#
# from pre import
# t = PrettyTable(['Name', 'Age'])
# t.add_row(['Alice', 24])
# t.add_row(['Bob', 19])
# print t


####################################################### Python to Excel
# import csv
#
# with open('Experiment.csv', 'w') as csv_infile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csv_infile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})



# import csv
# infile=open("BreakToLines_FourthDegree.txt","r")
# rows = [line.split() for line in infile]
# print(rows)
# with open("Experiment.csv", "w") as outfile:
#     writer = csv.writer(outfile)
#     writer.writerows(rows)
#
# infile.close()

# import csv
# infile=open("BreakToLines_FourthDegree.txt","r")
# rows = [line.split() for line in infile]
# with open("Experiment.csv", "a") as outfile:
#     writer = csv.writer(outfile, lineterminator='')
#     for val in rows:
#         writer.writerow([val])
#     writer.writerow("\n")
# infile.close()

####################################################### Beautifulsoup

# outfile=open("Experiment.txt","wb")
# import urllib.request
# with urllib.request.urlopen("http://www.python.org") as url:
#     s = url.read()
# #I'm guessing this would output the html source code?
# outfile.write(s)
# print(s)
# outfile.close()

####################################################### Lederman data

# outfile=open("Experiment.txt","wb")
# import urllib.request
# with urllib.request.urlopen("http://dt.lbc65.com/ViewDefendant.aspx?ID=304396") as url:
#     s = url.read()
# #I'm guessing this would output the html source code?
# outfile.write(s)
# print(s)
# outfile.close()

####################################################### Mutiple page and links experiment

# import urllib.request
# from bs4 import BeautifulSoup
#
# outfile = open('Experiment.txt', 'w')
#
# link = "http://espn.go.com/nba/team/roster/_/name/bkn/brooklyn-nets"
# page = urllib.request.urlopen(link)
# soup = BeautifulSoup(page, "html.parser")
# outfile.write(str(soup))
# # table = soup.find("table")
# # print(table)
# # for row in table.findAll("tr",{"class":["oddrow","evenrow"]}):
# #     col = row.findAll('td')
# #
# #     player = col[1].string
# #     position = col[2].string
# #     age=col[3].string
# #
# #     outfile.write(player + ',' + position + ',' + age + '\n')
#
# outfile.close()


from bs4 import *
import urllib.request
outfile = open('Experiment.txt', 'w')

link = "http://dt.lbc65.com/ViewDefendants.aspx?BondDate=10/10/2015"
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, "html.parser")
soup=soup.prettify()
outfile.write(str(soup))
# table = soup.find("table",{"class":["tb1NoPadding"]})
# print(table)
# for row_FD in table.find("tr"):
#     for row_SD in row_FD.findAll('td',{"class":["dxic"]}):
#         information=row_SD.findall("value")
#         outfile.write(information)
#     # name = col[1].string
#     # position = col[2].string
#     # age=col[3].string
#
#     # outfile.write(player + ',' + position + ',' + age + '\n')

outfile.close()



# #import urllib.request
# from bs4 import *
# import urllib.parse
# import urllib.request
# outfile = open('Experiment.txt', 'w')
# url = 'http://dt.lbc65.com/ViewDefendants.aspx?BondDate=10/10/2015'
# values = {'name' : 'Michael Foord',
#           'location' : 'Northampton',
#           'language' : 'Python' }
#
# data = urllib.parse.urlencode(values)
# data = data.encode('ascii') # data should be bytes
# req = urllib.request.Request(url, data)
# soup = BeautifulSoup(req, "html.parser")
# outfile.write(str(soup))
# outfile.close()



import urllib.request
import uuid
import os
import csv
import time