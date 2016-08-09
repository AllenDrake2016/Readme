####################################################### Quora

# import urllib.request
# from bs4 import BeautifulSoup
#
# link = "http://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup"
# page = urllib.request.urlopen(link)
# soup = BeautifulSoup(page, "html.parser")
# #outfile.write(str(soup))
# #input = soup.find("input",{'type':"hidden",'name':'_id_'})['value']
# input = soup.select("input")
# print(input)
# <input class="text_wide header_login_text_box ignore_interaction" group="__w2_CQInePF_interaction" type="text" placeholder="Email" name="email" w2cid="CQInePF" id="__w2_CQInePF_email">
# <input class="text_wide header_login_text_box ignore_interaction" group="__w2_CQInePF_interaction" type="password" placeholder="Password" name="password" w2cid="CQInePF" id="__w2_CQInePF_password">
# <input class="submit_button login_shift_right ignore_interaction" group="__w2_CQInePF_interaction" type="submit" value="Login" w2cid="CQInePF" id="__w2_CQInePF_submit_button">
# <input autocapitalize="off" autocorrect="off" autofocus="autofocus" class="form-control input-block" id="login_field" name="login" tabindex="1" type="text">
# <input class="form-control form-control input-block" id="password" name="password" tabindex="2" type="password">
# <input class="btn btn-primary btn-block" data-disable-with="Signing in…" name="commit" tabindex="3" type="submit" value="Sign in">

# import argparse
# import mechanicalsoup
# broswer = mechanicalsoup.Browser()
#
# parser = argparse.ArgumentParser()
# parser.add_argument("username",action="store")
# parser.add_argument("password",action="store")
# args = parser.parse_args(["zhhuangzihang@gmail.com","xisuo18EX@"])
#
# login_page = broswer.get("https://www.quora.com/topic/Logins")
# # soup = BeautifulSoup(login_page, "html.parser")
# #print(login_page.text)
# #login_form = login_page.soup.select("body")[0].select("div")[6].select("form")[0]
# #login_form = login_page.soup.select_one(".logged-out form")
# #login_form = login_page.soup.select_one(".auth-form form")
# #print(login_page)
# login_form = login_page.soup.select('form')
# #login_form=login_form.select('script', {'id': 'settings_js'})[0]
# print(login_form)
# login_form.find('input', {'name': 'email'})['value'] = args.username
# login_form.find('input', {'name': 'password'})['value'] = args.password
# page2 = broswer.submit(login_form, login_page.url)
#
#
# print(page2.text)



# import mechanicalsoup
# broswer = mechanicalsoup.Browser()
#
# login_page = broswer.get("https://www.quora.com/contact")
# login_form = login_page.soup.select('select')
# print(login_form)
# login_form = login_page.soup.select('option')
# print(login_form)
# print(login_form.attrs)
# # page2 = broswer.submit(login_form, login_page.url)
# # print(page2.text)

####################################################### Github

# import mechanicalsoup
# # response.css('base::attr(href)').extract()
#
#
# broswer = mechanicalsoup.Browser()
# login_page = broswer.get("https://github.com/login")
# login_form = login_page.soup.select("form")[0]
#
# # a=login_form.find('input', {'name': 'email'})
# # login_form.find('input', {'name': 'password'})['value']=123
# # b=login_form.find('input', {'name': 'password'})
# # print(a)
# # print(b)
#
# login_form.select("#login_field")[0]['value'] = 'Zihanghuang'
# login_form.select("#password")[0]['value'] = 'xisuo18EX@'
# page2 = broswer.submit(login_form, login_page.url)
#
# print(page2.text)
# # print(login_form)
# # # print(login_form.attrs)
# # print(login_page.url)

# UCP='652405002594'
# ZIP_CODE='07066'
# SITE_ADDR='http://www.barnesandnoble.com/w/16550798?ean='
# LINK_XPATH='/html/body/main/main/selection/div[1]/div/selection/aside/ul/li[1]/a'
#
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# class ScriapingBroswer(webdriver.Chrome):
#     def __init__(self,addr,upc,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.implicitly_wait(10)
#         self.get(addr+upc)
#
#     def enter_zip(self,zipcode):
#         self.find_element_by_xpath("/html/body/div[3]/div[0]/div[0]/div[0]").click()
#         self.find_element_by_name('zip').send_keys(zipcode,Keys.RETURN)
#
#     def switch_to_target_form(self):
#         iframe=None
#         while not iframe:
#             sleep(0.3)
#             for frame in self.find_element_by_tag_name('iframe'):
#                 if 'reservation.js' in str(frame.get_attribute('scr')):
#                     iframe=frame
#
#         self.switch_to.frame(iframe)
#
# if __name__=='__main__':
#     broswer=ScriapingBroswer(SITE_ADDR,UCP)
#     broswer.enter_zip(ZIP_CODE)
#     broswer.switch_to_target_form()


# chrome_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# driver=webdriver.ChromeOptions()
# driver.get()
#
#
# from lxml import etree
####################################################### Spider

# import os
#
# # Each website crawl is a seperate project(folder)
# def create_project_dir(directory):
#     if not os.path.exists(directory):
#         print('Creating project'+directory)
#         os.makedirs(directory)

def _build_request(**kwargs):
    data = kwargs.pop("data", dict())
    print(type(data))

_build_request()