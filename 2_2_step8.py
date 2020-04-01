from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element_by_css_selector("div.container div.form-group > [name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.container div.form-group > [name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.container div.form-group > [name='email']")
    input3.send_keys("Smolensk@mail.ru")



    element = browser.find_element_by_css_selector("#file")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, 'test.txt')
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()

