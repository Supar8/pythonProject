from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Nikolay")
    input2 = browser.find_element(By.NAME,"last_name")
    input2.send_keys("Kulagin")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Podgorica")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Monte")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
