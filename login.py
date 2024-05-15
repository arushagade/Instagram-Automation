from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to log in to Instagram and searching the username and liking post
def login_to_instagram(username, password):
    driver.get("https://www.instagram.com/")
    # Wait for the username field to be visible
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
    username_field.send_keys(username)

    # Wait for the password field to be visible
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
    password_field.send_keys(password)

    # Click on the login button
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()

    # Wait for the login process to complete
    WebDriverWait(driver, 10).until(EC.url_contains("instagram.com/accounts"))

# Initialize WebDriver
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Credentials
username = "project_learning_"
password = "arusha01"

# Login to Instagram
login_to_instagram(username, password)