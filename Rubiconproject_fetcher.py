from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

#Login
browser.get("https://platform.rubiconproject.com/#performance-analytics")
time.sleep(2)
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
username.send_keys("rg@4media-network.com")
password.send_keys("4M3d14nn")
login_attempt = browser.find_element_by_xpath("//a[text()='Log in']")
login_attempt.click()
time.sleep(2)

check_popup = (
    'var close_popUp = document.getElementsByClassName("walkme-custom-balloon-close-button")[0];'
    'if(close_popUp){'
    'close_popUp.click();'
'}'

)

time.sleep(10)
#Check updates
browser.execute_script(check_popup)

browser.switch_to.frame(browser.find_element_by_id("performance-analytics_iframe"))
## Choose publisher ##
elem = browser.find_element_by_id("context_publisher_18090")
elem.click()

## Switch back to the "default content" (that is, out of the iframes) ##
browser.switch_to.default_content()

time.sleep(5)
browser.switch_to.frame(browser.find_element_by_id("performance-analytics_iframe"))
browser.execute_script("document.querySelector('.dropdown.toolbar-btn.left.open-report .menu').style.display = 'block'")
time.sleep(2)
browser.execute_script("document.getElementById('load-saved-button').click()")
time.sleep(2)

try:
    report = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[text()="LukeReport_v2"]'))
    )
    report.click()
except OSError as err:
    print("OS error: {0}".format(err))

browser.execute_script("document.querySelectorAll('.dropdown.toolbar-btn .menu')[2].style.display = 'block'")

time.sleep(10)
try:
    report = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Export as Excel"]'))
    )
    report.click()
except OSError as err:
    print("OS error: {0}".format(err))

browser.switch_to.default_content()