from shutil import which
from pandas.io.pytables import dropna_doc
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options

# for waiting please import:
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import randint
import pandas as pd
import datetime
# from selenium.webdriver.common.proxy import Proxy, ProxyType
# proxy_ip_port = '115.85.73.179:3128'

# proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = proxy_ip_port
# proxy.ssl_proxy = proxy_ip_port

# capabilities = webdriver.DesiredCapabilities.CHROME
# proxy.add_to_capabilities(capabilities)
# chrome_options = Options()
# chrome_options.add_argument("--headless")

chrome_path = which("msedgedriver")
driver = webdriver.Edge(executable_path=chrome_path)

# driver.get('https://whatismyipaddress.com/')
    
# email = 'manicpanicdones@gmail.com'
# password = '5rVQ&FSR'
# email = 'richtips.services@gmail.com'
# # email = 'enlightenme.services@gmail.com'
# # email = 'lovefrom.blogger@gmail.com'
# # email = 'freetips.togrow@gmail.com'
# password = '123test456' 

# class login():
#     url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
#     driver.get(url)
#     driver.find_element_by_xpath("//*[@id='username']").send_keys(f"{email}")
#     driver.find_element_by_xpath("//*[@id='password']").send_keys(f"{password}")
#     sleep(randint(5,10))
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//button[@class='btn__primary--large from__button--floating']"))
#     )
#     element.click()

# login()
# sleep(randint(5,7))
# sleep(20)
df = pd.read_excel('combined_excel_linkedin.xlsx')

all_links = df['linkedin url'].tolist()[3950:3980]
first_nam = df['first name'].tolist()[1010:1040]
last_nam = df['last name'].tolist()[1010:1040]
role = df['role'].tolist()[1010:1040]
reaction = df['Reaction Type'].tolist()[1010:1040]
driver.get('https://www.linkedin.com/in/germandoms')
# driver.find_element_by_xpath("//button[@data-control-name='nav.settings']").click()
# sleep(0.5)
# driver.find_element_by_partial_link_text('Sign Out').click()
sleep(30)
x = datetime.datetime.now()
hour = x.hour
minute = x.minute
date_1= x.day
month = x.month
year = x.year
date_time1 = f'{year}-{month}-{date_1}_{hour}-{minute}'

data = []
list = {}
counter = 0
class work():
    for link,a,b,c,d in zip(all_links,first_nam,last_nam,role,reaction):
        counter += 1
        print(counter)
        driver.get(link)
        sleep(randint(8,12))
        driver.execute_script(f"window.scrollBy(0,700)","")
        sleep(1)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        try:
            # company_name = driver.find_element_by_xpath("//span[@class='text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view']").text.replace('"',' ')
            company_name = driver.find_element_by_xpath("//span[@class='top-card-link__description']").text.replace('"',' ')

        except:
            company_name = '-'
            pass
        try:
            # company_link = driver.find_element_by_xpath("//a[@data-control-name='background_details_company']").get_attribute("href")
            company_link = driver.find_element_by_xpath("//a[@class='result-card__subtitle-link ']").get_attribute("href")
        except:
            company_link = '-'
            pass
        
        try:
            # location = driver.find_element_by_xpath("//li[@class='t-16 t-black t-normal inline-block']").text.replace('"',' ')
            location = driver.find_element_by_xpath("//span[@class='top-card__subline-item']").text.replace('"',' ')
        except:
            location = '-'
            pass
        try:
            # connections = driver.find_element_by_xpath("//span[@class='t-16 t-black t-normal']").text
            connections = driver.find_element_by_xpath("//span[@class='top-card__subline-item top-card__subline-item--bullet']").text
        except:
            connections = '-'
            pass
        urls = link.split('?')[0]
        list = {
            'Linkedin Profile': urls,
            'First Name': a,
            'Last Name': b,
            'Reaction': d,
            'Current Company': company_name,
            'Company Linkedin URl': company_link,
            'Current Role': c,
            'Location': location,
            'Connections': connections
            
        }
        data.append(list)
        
        sleep(1)

work()
# login()
df = pd.DataFrame(data)
df.to_excel(f'Linkedin_{date_time1}.xlsx',encoding='utf-8', index=False)
# driver.close()

# sleep(120)

# df1 = pd.read_excel('combined_excel_linkedin.xlsx')

# all_links = df1['linkedin url'].tolist()[3920:3950]
# first_nam = df1['first name'].tolist()[1010:1040]
# last_nam = df1['last name'].tolist()[1010:1040]
# role = df1['role'].tolist()[1010:1040]
# reaction = df1['Reaction Type'].tolist()[1010:1040]
# # url = 'https://www.linkedin.com/'
# # driver.get(url)
# x = datetime.datetime.now()
# hour = x.hour
# minute = x.minute
# date_1= x.day
# month = x.month
# year = x.year
# date_time1 = f'{year}-{month}-{date_1}_{hour}-{minute}'

# data1 = []
# list1 = {}
# counter = 0
# class work1():
#     for link,a,b,c,d in zip(all_links,first_nam,last_nam,role,reaction):
#         counter += 1
#         print(counter)
#         driver.get(link)
#         sleep(randint(8,12))
#         driver.execute_script(f"window.scrollBy(0,700)","")
#         sleep(1)
#         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
#         try:
#             # company_name = driver.find_element_by_xpath("//span[@class='text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view']").text.replace('"',' ')
#             company_name = driver.find_element_by_xpath("//span[@class='top-card-link__description']").text.replace('"',' ')

#         except:
#             company_name = '-'
#             pass
#         try:
#             # company_link = driver.find_element_by_xpath("//a[@data-control-name='background_details_company']").get_attribute("href")
#             company_link = driver.find_element_by_xpath("//a[@class='result-card__subtitle-link ']").get_attribute("href")
#         except:
#             company_link = '-'
#             pass
        
#         try:
#             # location = driver.find_element_by_xpath("//li[@class='t-16 t-black t-normal inline-block']").text.replace('"',' ')
#             location = driver.find_element_by_xpath("//span[@class='top-card__subline-item']").text.replace('"',' ')
#         except:
#             location = '-'
#             pass
#         try:
#             # connections = driver.find_element_by_xpath("//span[@class='t-16 t-black t-normal']").text
#             connections = driver.find_element_by_xpath("//span[@class='top-card__subline-item top-card__subline-item--bullet']").text
#         except:
#             connections = '-'
#             pass
#         urls = link.split('?')[0]
#         list1 = {
#             'Linkedin Profile': urls,
#             'First Name': a,
#             'Last Name': b,
#             'Reaction': d,
#             'Current Company': company_name,
#             'Company Linkedin URl': company_link,
#             'Current Role': c,
#             'Location': location,
#             'Connections': connections
            
#         }
#         data1.append(list1)
        
#         sleep(1)

# work1()
# # login()



# df1 = pd.DataFrame(data1)
# df1.to_excel(f'Linkedin_{date_time1}.xlsx',encoding='utf-8', index=False)
# driver.close()
