# from selenium import webdriver
# driver = webdriver.Chrome('C:\\Users\\Administrator\\Desktop\\CS 065\\webchromedriver\\chromedriver.exe')
# driver.get('file:///C:/Users/Administrator/Desktop/.komodotools/IowaCourt/iowaCourt.html')


import os

list1=[]
list2=[]
infile=open('Research Box.txt','r')
for line in infile:
    caseNumber=line.replace('\n','')
    path='Data/'+caseNumber+'.txt'
    if os.path.isfile(path):
        list1.append(path)
        list2.append(caseNumber)

dictionary = dict(zip(list1, list2))

outfile=open('Data/query.html','w',encoding="utf-8")
outfile.write("<div>Allen's program gather all the research data into one page you may select the case filling you want to view by clicking the Menu.</div>"+'\n'+'<br/>')
outfile.write('<div id="top"></div>'+'\n')
for filename in list1:
    outfile.write('<details>' + '\n' +  '<summary class="summary">Menu</summary>' + '\n' + '<ul style="list-style: none; text-align:left;">')
    for CN in list2:
        outfile.write('<li><a href="query.html#'+CN+'">'+CN+'</a></li>'+'\n')
    outfile.write('</ul>'+'\n'+'</details>')
    with open(filename,'r') as f:
        outfile.write('<div id="' + dictionary[filename] + '"></div>'+'\n')
        for line in f:
            findnum1=line.find('<input name="logoffButton" type="submit" value="Logoff"/>')
            findnum2=line.find('<input name="changePassword" onclick="javaScript:goToPassword()" type="button" value="Change Password"/>')
            findnum3=line.find('Please Logoff when you are through accessing case detail information.')
            if findnum1==-1 and findnum2==-1 and findnum3==-1:
                outfile.write(line)
            elif findnum1!=-1:
                line=line.replace('<input name="logoffButton" type="submit" value="Logoff"/>','<a href="query.html#'+dictionary[filename]+'">Review this case</a></li>')
                outfile.write(line)
            elif findnum2!=-1:
                line=line.replace('<input name="changePassword" onclick="javaScript:goToPassword()" type="button" value="Change Password"/>','<a href="query.html#top">Go Back to the top</a></li>')
                outfile.write(line)
            elif findnum3!=-1:
                line=line.replace('Please Logoff when you are through accessing case detail information.','Click "Review this case" will bring you back to the top of this section while click "Go to the top" will bring you back to the top of this page.')
                outfile.write(line)
outfile.close()




