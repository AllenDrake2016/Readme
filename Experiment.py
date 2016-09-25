# def test_var_args(farg, *args):
#     print ("formal arg:", farg)
#     for arg in args:
#         print ("another arg:", arg)
#
# test_var_args(1, "two", 3)

# def test_var_kwargs(farg, **kwargs):
#     print ("formal arg:", farg)
#     for key in kwargs:
#         print ("another keyword arg:", kwargs[key])
#
# test_var_kwargs(farg=1, myarg2="two", myarg3=3)


# def test_var_kwargs(*arg, **kwargs):
#     print ("formal arg:", *arg)
#     for key in kwargs:
#         print ("another keyword arg:", kwargs[key])
#
# test_var_kwargs(1,2,3,4,arg=1, myarg2="two", myarg3=3)



# mylist = ['aardvark', 'baboon', 'cat']
# mydict = {'myarg3': 9}
# print(*mylist)
# print(**mydict)



# def myjobfunc(traj, extra_arg1, extra_arg2, extra_arg3):
#     # do some sophisticated simulation stuff
#     solve_p_equals_np(traj, extra_arg1)
#     disproof_spock(traj, extra_arg2, extra_arg3)
#
# def mypostproc(traj, postproc_arg1, postproc_arg2, postproc_arg3):
#     # do some analysis here
#     exploration_dict={'ncards' : [100, 200]}
#     if maybe_i_should_explore_more_cards:
#         return exploration_dict
#     else:
#         return None
#
#
#
# def mypipeline(traj):
#     # add some parameters
#     traj.f_add_parameter('poker.ncards', 7, comment='Usually we play 7-card-stud')
#
#     # Explore the trajectory
#     traj.f_explore({'ncards': range(42)})
#     # Finally return the tuples
#     args = (myarg1, myarg2) # myargX can be anything form ints to strings to complex objects
#     kwargs = {'extra_arg3': myarg3}
#     postproc_args = (some_other_arg1,) # Check out the comma here! Important to make it a tuple
#     postproc_kwargs = {'postproc_arg2' : some_other_arg2,'postproc_arg3' : some_other_arg3}
#     return (myjobfunc, args, kwargs), (mypostproc, postproc_args, postproc_kwargs)


# print("My name is %s" % "Allen")

####################################################### __init__

# from .Learning__init__ import Human
# class Lederman(Human):
#     def __init__(self,name,gender,information):
#         Human.__init__(self,name,gender)
#         self.information=information
#         #self.information=information
#
#     def input(self, data):
#         for (name, value) in data.items():
#             self.information.find("input", {"name": name})["value"] = value
#
#     def check(self, data):
#         for (name, value) in data.items():
#             if isinstance(value, list):
#                 for choice in value:
#                     self.information.find("input", {"name": name, "value": choice})[
#                         "checked"] = ""
#             else:
#                 self.information.find("input", {"name": name, "value": value})[
#                     "checked"] = ""
#
# #will=Human("william","Male","<input class='input1' id='input2' name='input3'>")
# will=Human("William","Male","<input class='input1' id='input2' name='input3' value='input4'>")
# print(will.name,will.gender)
# will.speak_name()
# def add(a,b):
#     return a+b
# value=will.math_task(add,4,5)
# print(value)



####################################################### .find

# a=Human(["<input class='input1' id='input2' name='input3' value='choice'>","<input class='input4' id='input5' name='input6' value='choice'>"],"Male")
# b=a.name.find("input",{"class":["input1"]})
# print(b)
# def check(self, data):
#     for (name, value) in data.items():
#         if isinstance(value, list):
#             for choice in value:
#                 self.information.find("input", {"name": name, "value": choice})[
#                     "checked"] = ""
#         else:
#             self.information.find("input", {"name": name, "value": value})[
#                 "checked"] = ""
#
#
# check(a)


# str1 = "this is string example....wow!!!"
# str2 = "exam"
# str1.items()
#
#
#
#
# print (str1.find(str2))
# print (str1.find(str2, 15))
# print (str1.find(str2, 40))


####################################################### .find

# d={1:'one',2:'two',3:'three'}
# print ('d.items():')
# for (k,v) in d.items():
#    if d[k] is v: print ('\tthey are the same object')
#    else: print ('\tthey are different')


# d=dict([('class','one'),('two',id),('value','three')])
# print ('d.items():')
# for (k,v) in d.items():
#    # if d[k] is v: print ('\tthey are the same object')
#    # else: print ('\tthey are different')
#    #print(k)
#    print(v)


# class Form(object):
#
#     def __init__(self, form):
#         self.form = form
#
#
#     # def input(self, data):
#     #     for (name, value) in data.items():
#     #         self.form.find("input", {"name": name})["value"] = value
#
#     # def check(self, data):
#     #     for (name, value) in data.items():
#     #         if isinstance(value, list):
#     #             for choice in value:
#     #                 val=self.form.find("input", {"name": name, "value": choice})["checked"]
#     #                 print(val)
#     #                 self.form.find("input", {"name": name, "value": choice})["checked"] = ""
#     #             else:
#     #                 self.form.find("input", {"name": name, "value": value})["checked"] = ""
#
#
# d=Form(dict([('input','four'),('class','one'),('two',id),('value','three')]))
# print(d.form)


####################################################### soup.find

# count=0
# while count<10:
#     count+=1
#     a=None
#     if count>5:
#         a=3
#     if a:
#         print("a exist")
#     else:
#         print("a does not exist")

####################################################### scrapy

#
# from scrapy.spider import BaseSpider
# from scrapy.selector import HtmlXPathSelector
# class Myspider(BaseSpider):
#    name='craig'
#    allowed_domains=['craigslist.org']
#    start_urls=["http://sfbay.craigslist.org/sfc/npo"]
#
#    def parse(self,response):
#       hxs=HtmlXPathSelector(response)
#       titles=hxs.select("//p")
#       print(titles)
#       for title in titles:
#           self.title=titles.select("a/text()").extract()
#           link=titles.select("a/@href").extract()
#           print title, link


# import scrapy
# class BlogSpider(scrapy.spider):
#    name='blogspider'
#    start_url=['http://blog.scrapinghub.com']
#    def parse(self,response):
#       for url in response.css('ul li a::attr("href")').re(r'.'/\d\d\d\d$'):
#          ye

# import os
# os.path.exists()
# from html.parser import HTMLParser
#
# class link(HTMLParser):
#     def handle_starttag(self, tag, attrs):


# a={}
# data = a.pop("data", dict())
# files = a.pop("files", dict())
# print(data)
# print(files)
# data = {
#     'authenticity_token': 'y6O8mKZ7n/jjb4Oz98I3HAA4sckEZsX7nyfYBqg0cqua2HcfV20nJv75/IV6+L3enIpv9nRqu0N+fPE2pRE7+g==',
#     'login': 'Zihanghuang', 'password': 'xisuo18EX@', 'utf8': '✓', 'commit': 'Sign in'}
# a["data"] = data
# print(a)
# def fun1(a="who is you", b="True", x, y):
#     print(a,b,x,y)

####################################################### selenium

# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome('C:\\Users\\Administrator\\Desktop\\CS 065\\chromedriver.exe')
# driver.get('https://www.quora.com/topic/Logins')
# time.sleep(5) # Let the user actually see something!
# # driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
# # search_box = driver.find_element_by_name('MsgId')
# # textarea=driver.find_element_by_tag_name('textarea')
# # textarea.send_keys('hello')
# button = driver.find_element_by_class("header_signin_with_search_bar action_button")
# button.click()
# time.sleep(5)
# driver.quit()

####################################################### selenium iowa online court
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\Administrator\\Desktop\\CS 065\\chromedriver.exe')
driver.get('https://www.iowacourts.state.ia.us/ESAWebApp/DefaultFrame')
time.sleep(5) # Let the user actually see something!
# textarea=driver.find_element_by_tag_name('textarea')
# textarea.send_keys('hello')
link = driver.find_element_by_link_text("Start A Case Search Here!")
link.click()
driver.get('https://www.iowacourts.state.ia.us/ESAWebApp/SelectAction')
driver.implicitly_wait(2)
# driver.switch_to.form=driver.find_element_by_tag_name('form')
form=driver.find_element_by_xpath("//form[@name='footerForm']")
button1=form.find_element_by_xpath("//input[@name='loginButton']")
button1.click()
user=driver.find_element_by_xpath('//input[@name="userid"]')
user.send_keys('Lederman2016')
user=driver.find_element_by_xpath('//input[@name="password"]')
user.send_keys('lovelydayisntit')
button2=driver.find_element_by_xpath('//input[@name="search"]')
button2.click()
driver.get('https://www.iowacourts.state.ia.us/ESAWebApp/TCaseAdvanced')
button3=driver.find_element_by_xpath('//select[@name="countydropdown"]')
# wrong code: 'button3.click()'
button4=button3.find_element_by_xpath('//option[@value="05771"]')
button4.click()


# infile=open("Case_number.txt","r")
# outfile=open("Case_number.txt","w")
# outfile.close()

# driver.get('https://www.iowacourts.state.ia.us/ESAWebApp/SelectAction')
# button_end=driver.find_element_by_xpath('//input[@name="logoffButton"]')
# button_end.click()
# time.sleep(2)
# driver.quit()


infile=open("Case_number.txt","r")
number=''
text=''
line=infile.readline()
for character in line:
    if character.isdigit():
        number+=character

    else:
        text+=character
text=text.strip('\n')
infile.close()
# print(number)
# print(text)

inputText=driver.find_element_by_xpath('//input[@name="caseid3"]')
inputText.click()
inputText.send_keys(text)
# inputText.send_keys(Keys.TAB)
inputNumber=driver.find_element_by_xpath('//input[@name="caseid4"]')
inputNumber.click()
inputNumber.send_keys(number)
inputNumber.send_keys(Keys.ENTER)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+Keys.PAGE_UP)
driver.switch_to_window(driver.window_handles[-1])
from selenium.webdriver.common.by import By
# driver.get('https://www.quora.com/topic/Logins')


form = driver.find_element_by_xpath("//form[@name='FinancialSummaryForm']")
trs=form.find_elements(By.XPATH,'//tr')

for tr in trs:
    find=False

    tds=tr.find_elements_by_tag_name('td')
    for td in tds:
        try:
            font=td.find_element_by_tag_name('font')

            if font.get_attribute('innerHTML')=='DEFENDANT':
                link_ID = tr.find_element_by_xpath('//td[@valign="top"]/font[1]')
                print('link is load')
                link_ID.click()
                find=True
                break



            else:
                print(font.get_attribute('innerHTML'))
        except:
            pass
    if find==True:
        break
driver.get('https://www.iowacourts.state.ia.us/ESAWebApp/TViewFilings')

    # font=trs.find_element_by_xpath('//font['+i+']')
    # if font.get_attribute('innerHTML')=='DEFENDANT':
    #     print('found it!!!!!!')
    #     print('font in text:')
    #     print(font.get_attribute('innerHTML'))
    #     # link_ID = tr.find_element_by_link_text('05771&nbsp;&nbsp;'+text+number)
    #     # link_ID.click()
    # else:
    #     print("fail")
    #     print(font.get_attribute('innerHTML'))

# # print(driver.page_source)
# # print(type(driver))
# print(font.get_attribute('innerHTML'))
# fonts=driver.find_elements(By.XPATH,'//font')
# for font in fonts:
#     print(font.get_attribute('innerHTML'))
# link=tr.find_element_by_link_text(text+number)



# form=driver.find_element_by_xpath('//form[@name="casesearch"]')
# submit=form.find_element_by_xpath('//input[@type="Submit"]')
# submit.click()
# time.sleep(5)
# submit2=submit
# submit2.click()
# infile=open("Case_number.txt","r")
# number=''
# text=''
# for data in infile:
#     line=infile.readline()
#     for character in line:
#         if character.isdigit():
#             number+=character
#
#         else:
#             text+=character
#
#     print('digi')
#     print(number)
#     print('none digi')
#     print(text)
#     number=''
#     text=''
# infile.close()