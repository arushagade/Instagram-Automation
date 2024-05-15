from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time

# Function to login to Instagram
def login(username, password):
    driver.get("https://www.instagram.com/")
    time.sleep(2)  # Let the page load

    # Find and fill in the username and password fields
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the form
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)  # Let the login process

# Function to comment on a post
def comment_post(post_url, comment_text):
    driver.get(post_url)
    time.sleep(2)  # Let the page load

    # Retry mechanism to locate the comment input field
    retries = 3
    while retries > 0:
        try:
            # Find the comment input field
            comment_input = driver.find_element(By.CSS_SELECTOR, "textarea[aria-label='Add a comment…']")
            # Type the comment and submit
            comment_input.send_keys(comment_text)
            comment_input.send_keys(Keys.RETURN)
            time.sleep(2)  # Let the action complete
            break
        except StaleElementReferenceException:
            retries -= 1
            if retries == 0:
                print("Failed to locate the comment input field after retries.")
                return

# Your Instagram credentials
username = "project_learning_"
password = "arusha01"

# URL of the post you want to comment on
post_url = "https://www.instagram.com/p/C3bBS5GAz6b/"

# Comment text
comment_text = "Your dedication and passion inspire us all to reach for greatness! Keep shining your light and showing us what's possible. You're making a real difference in the world!"

# Initialize Chrome WebDriver using ChromeDriverManager with options
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Log in to Instagram
login(username, password)

# Comment on the post
comment_post(post_url, comment_text)

time.sleep(20)