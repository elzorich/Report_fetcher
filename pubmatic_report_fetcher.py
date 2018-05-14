from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import shutil
import hashlib

browser = webdriver.Chrome()

#Login
browser.get("https://apps.pubmatic.com/login/publisher")
time.sleep(2)
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
username.send_keys("rg@4media-network.com")
password.send_keys("4m3diA_Net")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
time.sleep(15)

#Go to Analytics
try:
    analytics = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="Analytics"]'))
    )
    analytics.click()
except OSError as err:
    print("OS error: {0}".format(err))


#Go to Custom reports
try:
    custom = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Custom")]'))
    )
    custom.click()
except OSError as err:
    print("OS error: {0}".format(err))


#Find Daily Revenue Report
report = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Daily Revenue Report")]'))
    )
#Find it's parent row
rowElement = report.find_element_by_xpath(".//ancestor::div[2]")
button = WebDriverWait(rowElement, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Download")]'))
    )
#Click the download button
browser.execute_script("document.querySelectorAll('button.pmcc-btn-sm.pmcc-secondary.ng-scope')[11].click()")

time.sleep(5)

#Take the latest report
browser.execute_script("document.querySelectorAll('button.pmcc-btn-sm.pmcc-secondary')[1].click()")

time.sleep(10)

#Get SHA1 hash of file contents
def file_hash(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb', buffering=0) as f:
        for b in iter(lambda: f.read(128*1024), b''):
            h.update(b)
    return h.hexdigest()


#Open a file, specify path for download file
path = "C:/Users/Elena/Downloads"

#Specify new path for download and renamed file
new_path = 'C:/!Doc/ESL/4MediaNetwork/Pubmatic/Pubmatic_report'

#Get last downloaded file
filename = max([path + "/" +  f for f in os.listdir(path)], key=os.path.getctime)

datestamp = time.strftime("%Y-%m-%d")
publisher = 'Pubmatic'
hash = file_hash(filename)
print(hash)
status = ''
ext = '.csv'
new_name = datestamp + '_' + publisher + '_' + hash + status + ext

shutil.move(os.path.join(new_path,filename),new_name)













