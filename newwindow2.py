import os, math, time
from selenium import webdriver
browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



button = browser.find_element_by_css_selector("button.btn")
button.click()



new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


time.sleep(2)





#alert = browser.switch_to.alert
#alert.accept()

x = browser.find_element_by_css_selector("#input_value")

form = browser.find_element_by_css_selector("#answer")

form.send_keys(calc(x.text))

button = browser.find_element_by_css_selector("button.btn")
button.click()
