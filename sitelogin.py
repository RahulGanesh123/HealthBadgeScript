from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/rahulganesh/Desktop/Projects/sitelogin/chromedriver")
url = 'https://canvas.ucsc.edu/courses/53169/announcements'
driver.get(url)
username = 'canvas login username'
pswd = 'canvas login pswd'
fillname = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
fillpswd = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(pswd)
clickbtn = driver.find_element(By.XPATH, '/html/body/section/div/form/button').click()
assignments = driver.find_elements(By.CLASS_NAME, 'ic-item-row ic-announcement-row')
print("Announcements: ", assignments, "Length: ", len(assignments))
