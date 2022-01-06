# WEB TOOL FOR CREATING ACCOUNTS
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import time

driver = webdriver.Chrome()

driver.get("https://glorysmacks.com/signup/create")
xpath_mail = '//*[@id="pageContent"]/div/div/div[1]/div/input'
#driver.find_element_by_xpath(xpath_mail).send_keys("ciguelpanilas@gmail.com")
driver.find_element(By.XPATH, (xpath_mail)).send_keys("ciguelpanilas@gmail.com")

xpath_pw = '//*[@id="pageContent"]/div/div/div[2]/div/input'
#driver.find_element_by_xpath(xpath_pw).send_keys("conacona123")
driver.find_element(By.XPATH, (xpath_pw)).send_keys("conacona123")

cbox_path = '//*[@id="pageContent"]/div/div/div[3]/div'
#button = driver.find_element_by_xpath(cbox_path)
button = driver.find_element(By.XPATH, (cbox_path))
driver.execute_script("arguments[0].click();", button)

#css_selector_area = '#pageContent > div > div > div.jss50.PhoneInput > div > select'
#driver.find_element_by_css_selector(css_selector_area).send_keys('Russia')



# Select country
#country = Select(driver.find_element_by_))
#country.select_by_visible_text('Russia')

#time.sleep(3)

#area_button_one = driver.find_elements_by_class_name('PhoneInputCountrySelectArrow')
#pick = Select(area_button_one)
#flag_list = pick.options
#print(len(flag_list))



# Select country
#xpath_area = '//*[@id="pageContent"]/div/div/div[1]/div/select' # --> program closes before opening country page
##area_button = driver.find_element(By.XPATH, (xpath_area))#.send_keys('Russia') # --> program open country page but does not select country box
#driver.find_element(By.XPATH, (xpath_area))
#driver.execute_script("arguments[0].click();", area_button)
#time.sleep(2)

#select = Select(driver.find_element_by_xpath(xpath_area))
#select.select_by_visible_text('Russia')

#select = Select(driver.find_element_by_find_element_by_css_selector(css_selector_area)
#select.select_by_visible_text('Russia')

# driver.find_element_by_xpath(xpath_area).click()
# driver.execute_script("arguments[0].click();", button_area);  # --> doesn't work, still doesnt click country box
# driver.execute_script("arguments[0].click();", button);
