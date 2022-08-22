from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()

page = driver.get('https://www.instagram.com')

sleep(90)

username_textfield = driver.find_element_by_name('username')

password = driver.find_element_by_name('password')

login_button = driver.find_element_by_class_name('sqdOP  L3NKy   y3zKF     ')

username_textfield.click()
username_textfield.sendkeys('')
sleep(5)

password.click()
password.sendkeys('')

sleep(5)

login.button.click()
