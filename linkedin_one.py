from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# for waiting please import:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import randint
import pandas as pd

chrome_options = Options()
# chrome_options.add_argument("--headless")

chrome_path = which("chromedriver")
driver = webdriver.Chrome(executable_path=chrome_path, options= chrome_options)
url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
driver.get(url)


class login():
    driver.find_element_by_xpath("//*[@id='username']").send_keys("banglabokbok420@gmail.com")
    driver.find_element_by_xpath("//*[@id='password']").send_keys("5rVQ&FSR")
    sleep(randint(10,15))
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn__primary--large from__button--floating']"))
    )
    element.click()

login()
sleep(randint(3,5))

driver.get('https://www.linkedin.com/posts/soy-startup_emprendimiento-startups-rappi-activity-6773987304848601088-BZNt/')

sleep(randint(2,5))
driver.find_element_by_xpath("//span[@class='v-align-middle social-details-social-counts__reactions-count']").click()

sleep(randint(2,5))

# clap = driver.find_element_by_xpath("//button[@class='ml0 p3 artdeco-tab ember-view']").click()
link = driver.find_elements_by_xpath("//button[@class='ml0 p3 artdeco-tab ember-view']")[5].click()


fBody  = driver.find_element_by_xpath("//div[@class='artdeco-modal__content social-details-reactors-modal__content ember-view']")
sleep(0.5)

scroll = 0
try:
    while scroll < 10: # scroll 5 times
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        sleep(randint(1,3))
        scroll += 1
        print(scroll)
except:
    pass

data = []
list = {}
links = driver.find_elements_by_xpath("//li[@class='artdeco-list__item ']/a")
names = driver.find_elements_by_xpath("//li[@class='artdeco-list__item ']/a/div/div[2]/div[1]/span")
current_roles = driver.find_elements_by_xpath("//li[@class='artdeco-list__item ']/a/div/div[2]/div[3]")
for link,name,current_role in zip(links,names,current_roles):
    profile_link = link.get_attribute("href")
    name1 = name.text.split(' ')
    name2 = name.text
    first_name = name1[0]
    last_name = name2.replace(f'{first_name}',' ')
    role = current_role.text.replace('"',' ')
    # type = 'Support'
    list = {
        'linkedin url': profile_link,
        'first name': first_name,
        'last name': last_name,
        'role': role,
        'Reaction Type': 'Insightful'
    }
    data.append(list)
df = pd.DataFrame(data)
df.to_excel(f'4_data_linkedin_insightful.xlsx',encoding='utf-8-sig', index=False)

