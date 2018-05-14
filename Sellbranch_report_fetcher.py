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
browser.get("https://360yield.com/login")
time.sleep(2)
username = browser.find_element_by_id("login__username-inputEl")
password = browser.find_element_by_id("login__password-inputEl")
username.send_keys("rg@4media-network.com")
password.send_keys("Sellbranch_2016_M")
login_attempt = browser.find_element_by_id("login_submit_form_btn")
login_attempt.click()
time.sleep(5)

press_weekly = (
    'var elements = document.getElementsByClassName("x-btn-inner-default-toolbar-small");'
    'for(var i = 0, len = elements.length; i < len; i++){'
	    'if(elements[i].innerHTML == "Weekly"){'
            'elements[i].click();'
    '}'
    '}'
)

press_daily = (
    'var elements = document.getElementsByClassName("x-btn-inner-default-toolbar-small");'
    'for(var i = 0, len = elements.length; i < len; i++){'
	    'if(elements[i].innerHTML == "Daily"){'
            'elements[i].click();'
    '}'
    '}'
)

press_generate_report = (
    'var elements = document.getElementsByClassName("x-btn-inner-id-ui-green-button-small");'
    'for(var i = 0, len = elements.length; i < len; i++){'
	    'if(elements[i].innerHTML == "Generate 360 report"){'
            'elements[i].click();'
    '}'
    '}'
)

press_export_excl = (
    'var elements = document.getElementsByClassName("x-btn-inner-id-ui-green-button-small");'
    'for(var i = 0, len = elements.length; i < len; i++){'
	    'if(elements[i].innerHTML == "Export to Excel"){'
            'elements[i].click();'
    '}'
    '}'
)

press_dimension = (
    'var element = document.querySelector(\'div[id^="chart-filter"] div[id$="trigger-picker"]\');'
    'element.click();'
)

boundlist_dimension = (
    'var elements = document.querySelectorAll(\'div[id^="boundlist"] .x-boundlist-item\');'
    'for(var i = 0, len = elements.length; i < len; i++){'
	    'if(elements[i].innerHTML == "Site"){'
            'elements[i].click();'
            '}'
    '}'

)

press_Metric_A = (
    'var element = document.querySelectorAll(\'.x-form-item-body.x-form-item-body-id-ui-form-combobox-field.x-form-text-field-body.x-form-text-field-body-id-ui-form-combobox-field[id^="combo"]'
    '   div[id$="trigger-picker"]\')[4];'
    'element.click();'
)


boundlist_Metric_A = (

    'elements = document.querySelectorAll(".x-boundlist");'
    'for(var i = 0, len = elements.length; i < len; i++){'
	'var style = getComputedStyle(elements[i]);'
	   'if (style.display === "none" ) {'

            '}'
		'else{console.log(elements[i].querySelectorAll(\'div[id^="boundlist"] .x-boundlist-item\'));'
        'var boundlist_li = elements[i].querySelectorAll(\'div[id^="boundlist"] .x-boundlist-item\');'
        'for(var i = 0, len = boundlist_li.length; i < len; i++){'
	    'if(boundlist_li[i].innerHTML == "Paid impressions"){'
            'boundlist_li[i].click();'
            '}'
    '}'
'}'
    '}'

)

press_Metric_B = (
    'var element = document.querySelectorAll(\'.x-form-item-body.x-form-item-body-id-ui-form-combobox-field.x-form-text-field-body.x-form-text-field-body-id-ui-form-combobox-field[id^="combo"]'
    '   div[id$="trigger-picker"]\')[5];'
    'element.click();'
)

boundlist_Metric_B = (
    'elements = document.querySelectorAll(".x-boundlist");'
    'for(var i = 0, len = elements.length; i < len; i++){'
	'var style = getComputedStyle(elements[i]);'
	   'if (style.display === "none" ) {'
            '}'
		'else{console.log(elements[i].querySelectorAll(\'div[id^="boundlist"] .x-boundlist-item\'));'
        'var boundlist_li = elements[i].querySelectorAll(\'div[id^="boundlist"] .x-boundlist-item\');'
        'for(var i = 0, len = boundlist_li.length; i < len; i++){'
	    'if(boundlist_li[i].innerHTML == "Revenue"){'
            'boundlist_li[i].click();'
            '}'
    '}'
'}'
    '}'

)


#Go to Reports
try:
    reports = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.ID, 'reports_tab'))
    )
    reports.click()
except OSError as err:
    print("OS error: {0}".format(err))

time.sleep(10)
#Go to Weekly report
browser.execute_script(press_weekly)

time.sleep(1)
#Click Dimension
browser.execute_script(press_dimension)

time.sleep(1)
#Choose Dimension -> Site
browser.execute_script(boundlist_dimension)

time.sleep(1)
#Click Metric_A
browser.execute_script(press_Metric_A)

time.sleep(1)
#Choose Metric_A -> 'Paid impressions'
browser.execute_script(boundlist_Metric_A)

time.sleep(1)
#Click Metric_B
browser.execute_script(press_Metric_B)

time.sleep(1)
#Choose Metric_B-> 'Revenue'
browser.execute_script(boundlist_Metric_B)

time.sleep(1)
#Go to Daily report
browser.execute_script(press_daily)

time.sleep(1)
#Generate report
browser.execute_script(press_generate_report)

time.sleep(1)
#Export to excel
browser.execute_script(press_export_excl)

time.sleep(10)

#Get SHA1 hash of file contents
def file_hash(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb', buffering=0) as f:
        for b in iter(lambda: f.read(128*1024), b''):
            h.update(b)
    return h.hexdigest()


#Specify path for downloaded file
path = "C:/Users/Elena/Downloads"

#Specify new path for download and renamed file
new_path = 'C:/!Doc/ESL/4MediaNetwork/Pubmatic/Pubmatic_report'

#Get last downloaded file
filename = max([path + "/" +  f for f in os.listdir(path)], key=os.path.getctime)


datestamp = time.strftime("%Y-%m-%d")
publisher = 'Sellbranch'
hash = file_hash(filename)
status = ''
ext = '.xlsx'
new_name = datestamp + '_' + publisher + '_' + hash + status + ext

shutil.move(os.path.join(new_path,filename),new_name)



