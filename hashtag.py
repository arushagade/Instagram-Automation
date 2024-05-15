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

# Initialize Chrome WebDriver using ChromeDriverManager with options
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Your Instagram credentials
username = "project_learning_"
password = "arusha01"

# Log in to Instagram
login(username, password)

# Define the hashtag you want to research
hashtag = 'computerengineering'

# Open Instagram website
driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")

try:
    # Wait for the top posts to load
    top_posts = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//article[@class='ySN3v']")))
    
    # Print information about each top post
    for post in top_posts:
        likes = post.find_element(By.XPATH, ".//span[@class='zV_Nj']/span").text
        comments = post.find_element(By.XPATH, ".//span[@class='u-__7']").text
        caption = post.find_element(By.XPATH, ".//div[@class='C4VMK']/span").text
        url = post.find_element(By.XPATH, ".//a").get_attribute('href')
        owner = post.find_element(By.XPATH, ".//div[@class='e1e1d']/span/a").get_attribute('title')
        profile_url = f"https://www.instagram.com/{owner}/"
        
        print("Likes:", likes)
        print("Comments:", comments)
        print("Caption:", caption)
        print("URL:", url)
        print("Owner:", owner)
        print("Profile URL:", profile_url)
        print()
    
except Exception as e:
    print("Error:", e)

time.sleep(100)