from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    sunduk = browser.find_element_by_css_selector("#treasure")
    x = sunduk.get_attribute("valuex")
    y = calc(x)

    input_form = browser.find_element_by_css_selector("#answer")
    input_form.send_keys(y)
    imnot = browser.find_element_by_css_selector("#robotCheckbox")
    imnot.click()


    robotrules = browser.find_element_by_css_selector("[value='robots']")
    robotrules.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)


finally:
    time.sleep(5)
    browser.quit()