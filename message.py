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

def send_message_to_user(username, message):
    # Navigate to user's profile
    driver.get(f"https://www.instagram.com/{username}/")
    time.sleep(2)
    # Click on the message button
    message_button = driver.find_element(By.CSS_SELECTOR, "div[role='button']")
    message_button.click()
    time.sleep(2)
    # Wait for the message input box to be clickable
    # message_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[placeholder='Message...']")))
    message_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Message']")))
    message_input.send_keys(message)
    time.sleep(1)

    driver.find_element(By.XPATH,"""/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]""").click()
    #send button code
    driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]""").click()
    time.sleep(2)
 
# Initialize WebDriver
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Credentials
username = "project_learning_"
password = "arusha01"

# Login to Instagram
login_to_instagram(username, password)

# Message someone
recipient_username = "bhakti_darawade"
message = "Hello! Just wanted to drop you a quick note to say hello and wish you a wonderful day ahead! This message is automated, but the warm wishes are genuine. Take care!"
send_message_to_user(recipient_username, message)

time.sleep(100)