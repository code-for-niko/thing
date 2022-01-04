from selenium import webdriver
from time import time 

driver = webdriver.Chrome()

driver.get("https://glorysmacks.com/signup/create")
xpath_mail = '//*[@id="pageContent"]/div/div/div[1]/div/input'
driver.find_element_by_xpath(xpath_mail).send_keys("ciguelaneleiro@gmail.com")

xpath_pw = '//*[@id="pageContent"]/div/div/div[2]/div/input'
driver.find_element_by_xpath(xpath_pw).send_keys("conacona123")

cbox_path = '//*[@id="pageContent"]/div/div/div[3]/div'
button = driver.find_element_by_xpath(cbox_path)
driver.execute_script("arguments[0].click();", button);


#xpath_area = '//*[@id="pageContent"]/div/div/div[1]/div/select' # --> program closes before opening country page
xpath_area = '//*[@id="pageContent"]/div/div/div[1]'
driver.find_element_by_xpath(xpath_area).send_keys # --> program open country page but does not select country box
# solution 01 #
#button_area =#
driver.find_element_by_xpath(xpath_area).click()
#driver.execute_script("arguments[0].click();", button_area);  # --> doesn't work, still doesnt click country box

#driver.execute_script("arguments[0].click();", button);



