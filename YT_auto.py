from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# class Music():
def play(query):
    driver = webdriver.Chrome()  # Ensure the chromedriver path is correct and it is installed
    driver.get(f"https://www.youtube.com/results?search_query=" + query)

    # Wait for the user to press Enter the console to close the browser
    input("Press Enter to close the browser and exit...")

    driver.quit()
