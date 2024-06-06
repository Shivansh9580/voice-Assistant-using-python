from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class info():
    def __init__(self):
        s = Service('C:\webdriver\chromedriver-win32\chromedriver-win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org/")
        search=self.driver.find_element(by=By.XPATH, value='//*[@id="search-input"]')
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element(by=By.XPATH, value='//*[@id="search-form"]/fieldset/button')
        enter.click()







# s = Service('C:\webdriver\chromedriver-win32\chromedriver-win32\chromedriver.exe')
#
# driver = webdriver.Chrome(service=s)
# driver.get("https://www.google.com")
#
# the_url= driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]")
#
# driver.quit()

# class info():
#     def __init__(self):
#         self.driver=webdriver.Chrome(service='C:\webdriver\chromedriver-win32\chromedriver-win32\chromedriver.exe')
#
#     def get_info(self,query):
#         self.query=query
#         self.driver.get(url="https://www.google.com")
#
# assist=info()
# assist.get_info('heelo')

