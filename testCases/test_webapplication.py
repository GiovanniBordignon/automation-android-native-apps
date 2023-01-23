from appium import webdriver
import time

desire_caps = dict(
    deviceName = 'Android',
    platformName = 'Android',
    browserName = 'Chrome',
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)


driver.get('http://www.amazon.com')
time.sleep(2)

driver.quit()