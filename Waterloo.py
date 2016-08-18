import urllib.request
from bs4 import BeautifulSoup

link = "http://www.bhcso.org/WhosInJail.aspx"
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, "html.parser")
#outfile.write(str(soup))
td = soup.find("td",{"colspan":["5"]})
#print(td)
for row in td.findAll("a"):
    print(row.attrs['href'])
    link = row.attrs['href']
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page, "html.parser")
    print(soup)

import mechanicalsoup
