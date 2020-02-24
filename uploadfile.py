import os 
from selenium import webdriver
browser = webdriver.Chrome()





link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

input1 = browser.find_element_by_css_selector('[name="firstname"]')
input2 = browser.find_element_by_css_selector('[name="lastname"]')
input3 = browser.find_element_by_css_selector('[name="email"]')
input1.send_keys("Ivan")
input2.send_keys("Petrov")
input3.send_keys("ivan@petrov.ru")




input4 = browser.find_element_by_css_selector('[type="file"]')
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
input4.send_keys(file_path)
button = browser.find_element_by_css_selector("button.btn")
button.click()