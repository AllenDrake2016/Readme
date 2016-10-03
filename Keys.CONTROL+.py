# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome('C:\\Users\\Administrator\\Desktop\\CS 065\\chromedriver.exe')
# driver.get('https://www.quora.com/topic/Logins')
# body=driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')
# driver.get('https://bing.com')
#
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+Keys.PAGE_UP)
# driver.switch_to_window(driver.window_handles[-1])
# print(driver.page_source)
# # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'w')
# infile=open("Case_number.txt","r")
# number=''
# text=''
# line=infile.readline()
# for character in line:
#     if character.isdigit():
#         number+=character
#
#     else:
#         text+=character
# text=text.strip('\n')
# infile.close()
# a='05771&nbsp;&nbsp;'+text+number
# print(a)
#######################################################


