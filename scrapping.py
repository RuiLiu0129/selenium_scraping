from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs
import time

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome(executable_path='/Users/ruiliu/anaconda3/envs/selenium/bin/chromedriver', chrome_options=option)

# Go to desired website
browser.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
assert "Login" in browser.title

# Complete the username and password fields
username = browser.find_element_by_id("username")
username.clear()
username.send_keys("rl2987@columbia.edu")

password = browser.find_element_by_id("password")
password.clear()
password.send_keys("Lriuui_172301")

# Click the sign in button
browser.find_element_by_xpath("//button[@type='submit']").click()
timeout = 2000

# open homepage
browser.find_element_by_xpath("//a[@data-control-name='identity_profile_photo']").click()


# Get the name
wait = WebDriverWait(browser, 10)
names_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h1.pv-top-card-section__name")))
print(names_element.text)


# Get description
description_elements = browser.find_element_by_css_selector("p.pv-top-card-section__summary-text")
print(description_elements.text)


# Get experience
wait = WebDriverWait(browser, 30)
time.sleep(20)
experience_elements = wait.until(EC.visibility_of_element_located((By.XPATH, "//div/span/div/section/div/section[@id='experience-section']")))
print(experience_elements.text)


# Get education
wait = WebDriverWait(browser,20)
education_elements = wait.until(EC.element_to_be_clickable((By.ID, "education-section")))
print(education_elements.text)

# Get Volunteer Experience
wait = WebDriverWait(browser,20)
volunteer_elements = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"pv-profile-section volunteering-section ember-view")))
print(volunteer_elements.text)

# Got Skills
wait = WebDriverWait(browser,20)
skills_elements = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"pv-profile-section pv-skill-categories-section artdeco-container-card ember-view")))
print(skills_elements.text)

# Got accomplishments
wait = WebDriverWait(browser,20)
accomplishments_elements = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"pv-profile-section pv-accomplishments-section artdeco-container-card ember-view")))
print(accomplishments_elements.text)

# click to another user
wait = WebDriverWait(browser,20)
user_elements = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"name-and-distance"))).click()




