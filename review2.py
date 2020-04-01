from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)


input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
input1.send_keys("Vladislav")
input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
input2.send_keys("Repin")
input3 = browser.find_element_by_css_selector("input.form-control.third")
input3.send_keys("onimuska@mail.ru")


button = browser.find_element_by_css_selector("button.btn")
button.click()


time.sleep(5)


welcome_text_elt = browser.find_element_by_tag_name("h1")

welcome_text = welcome_text_elt.text


assert "Congratulations! You have successfully registered!" == welcome_text


time.sleep(10)
browser.quit()
