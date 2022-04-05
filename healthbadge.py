from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from subprocess import call
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders




driver = webdriver.Chrome(executable_path="/Users/rahulganesh/Desktop/Projects/sitelogin/chromedriver")
url = 'https://studenthealth.ucsc.edu/?_gl=1*1k2r5wh*_ga*MTg2NjExMTE4NC4xNjQ5MTA3MjEx*_ga_BWJ4Z4Y66X*MTY0OTEwNzIxMC4xLjEuMTY0OTEwNzI1MS4w'
driver.get(url)
username = 'raganesh'
pswd = 'Sashapwd123!'
fillname = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
fillpswd = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(pswd)
clickbtn = driver.find_element(By.XPATH, '/html/body/section/div/form/button').click()
driver.implicitly_wait(20)
dateofbirth = '07/18/2003'
filldate = driver.find_element(By.XPATH, '//*[@id="dtDOB"]').send_keys(dateofbirth)
clicknext = driver.find_element(By.XPATH, '//*[@id="cmdStandardProceed"]').click()
clickfinal = driver.find_element(By.XPATH, '//*[@id="ctl03"]/div[2]/a').click()
#pyautogui.screenshot('/System/Applications/Photos.app/image1.png')
driver.fullscreen_window()
time.sleep(2)
call(["screencapture", "screenshot.jpg"])

#Now email myself the image
email_user = 'badgehealth@gmail.com'
email_password = 'green123!'
email_send = 'badgehealth@gmail.com'

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

filename='screenshot.jpg'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()

#Script only needs to run every 24 hours, in the morning only
