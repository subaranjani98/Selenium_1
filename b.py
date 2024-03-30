from selenium import webdriver
from selenium.webdriver.common.by import By

# Setting up Chrome WebDriver
driver = webdriver.Chrome()

# Opening the URL
driver.get("https://www.saucedemo.com/")

# Finding username and password input fields, and login button
username_input = driver.find_element(By.ID,"user-name")
password_input = driver.find_element(By.ID,"password")
login_button = driver.find_element(By.ID,"login-button")

# Entering credentials and submitting the form
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()

# Task 1: Get title of the webpage
title = driver.title
print("Title:", title)

# Task 2: Get current URL of the webpage
current_url = driver.current_url
print("Current URL:", current_url)

# Task 3: Extract entire contents of the webpage and save it in a text file
contents = driver.find_element(By.TAG_NAME,"body").text
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(contents)

# Closing the browser
driver.quit()