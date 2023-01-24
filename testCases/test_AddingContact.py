import time
from appium import webdriver
from selenium.webdriver.common.by import By

desire_caps = dict(
    deviceName = 'Android',
    platformName = 'Android',
    appPackage = 'com.android.contacts',
    appActivity = 'com.android.contacts.activities.PeopleActivity'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

driver.find_element(By.ID, 'com.android.contacts:id/floating_action_button_container').click()
time.sleep(1)
driver.find_element(By.ID, 'com.android.contacts:id/left_button').click()
# In this case, i'll use the 'send_keys()' function. However, it's possible to type in the device's keyboard.
driver.find_element(By.XPATH, '//android.widget.EditText[@text="First name"]').send_keys('Peter')
driver.find_element(By.XPATH, '//android.widget.EditText[@text="Last name"]').send_keys('Parker')
driver.find_element(By.XPATH, '//android.widget.EditText[@text="Phone"]').send_keys('99887766')
driver.find_element(By.ID, 'com.android.contacts:id/editor_menu_save_button').click()

time.sleep(2)
driver.quit()