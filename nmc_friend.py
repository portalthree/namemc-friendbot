from time import sleep
from selenium import webdriver
import requests

driver = webdriver.Chrome(executable_path=r'C:\Users\User\Documents\chromedriver_win32\chromedriver.exe')
driver.set_window_size(1920, 1040)
driver.get("https://namemc.com/login")
print("enter " + driver.title)
sleep(7)

# LOGIN NAMEMC
# email
driver.find_element_by_id("email").send_keys("EMAIL@domain.com")
sleep(0.3)

# password
driver.find_element_by_id("password").send_keys("ENTER YOUR PASSWORD HERE")
sleep(0.5)

# login button click
driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[2]/form/div/button").click()
print("login ok")
sleep(1)

r = requests.get("https://api.namemc.com/profile/403e6cb7-a6ca-440a-8041-7fb1e579b5a5/friends")

events = r.json()
for event in events:
    try:
        print(event['name'])
        driver.get("https://namemc.com/profile/" + event['name'])
        sleep(10)
        driver.find_element_by_css_selector('#add-friend-button').click()
        print("Added as a friend !")
        sleep(30)
    except:
        print("You already friended this person.")
        continue
