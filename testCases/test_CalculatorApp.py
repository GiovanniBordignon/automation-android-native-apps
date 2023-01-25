import time
from appium import webdriver
from selenium.webdriver.common.by import By

desire_caps = dict(
    deviceName = 'Android',
    platformName = 'Android',
    appPackage = 'com.google.android.calculator',
    appActivity = 'com.android.calculator2.Calculator'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

driver.find_element(By.ID, 'com.google.android.calculator:id/digit_2').click()
driver.find_element(By.ID, 'com.google.android.calculator:id/op_mul').click()
driver.find_element(By.ID, 'com.google.android.calculator:id/digit_4').click()
driver.find_element(By.ID, 'com.google.android.calculator:id/eq').click()

result = driver.find_element(By.ID, 'com.google.android.calculator:id/result_final').text
print(result)


time.sleep(2)
driver.quit()