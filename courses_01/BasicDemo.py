"""
Basic Demo for Python Seleinum.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

driver = webdriver.Remote(
   command_executor='http://0.0.0.0:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.FIREFOX)
driver.get("https://www.baidu.com")
elem = driver.find_element_by_id('kw')
elem.send_keys('Robot Framework')
driver.find_element_by_id('su').click()
sleep(10)
driver.close()


