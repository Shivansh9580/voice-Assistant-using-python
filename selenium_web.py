from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# class Info():
def get_info(query):
    driver = webdriver.Chrome()  # Ensure the chromedriver path is correct and it is installed
    driver.get(f"https://en.wikipedia.org/wiki/{query}")

    # Wait for the user to press Enter the console to close the browser
    input("Press Enter to close the browser and exit...")

    driver.quit()


