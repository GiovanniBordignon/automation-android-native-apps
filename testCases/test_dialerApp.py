import time
from appium import webdriver
from selenium.webdriver.common.by import By

desire_caps = dict(
    deviceName = 'Android',
    platformName = 'Android',
    appPackage = 'com.android.dialer',
    appActivity = 'com.android.dialer.main.impl.MainActivity'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

driver.find_element(By.ID, 'com.android.dialer:id/fab').click()
time.sleep(1)
# Time sleep isn't the best choice but works. Later i'm planning to introduce a more sophisticated solution.
driver.find_element(By.ID, 'com.android.dialer:id/one').click()
driver.find_element(By.ID, 'com.android.dialer:id/two').click()
driver.find_element(By.ID, 'com.android.dialer:id/three').click()
driver.find_element(By.ID, 'com.android.dialer:id/four').click()
driver.find_element(By.ID, 'com.android.dialer:id/dialpad_floating_action_button').click()
time.sleep(3)
driver.find_element(By.ID, 'com.android.dialer:id/incall_end_call').click()

time.sleep(2)
driver.quit()