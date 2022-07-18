from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.booking.com")
get_element = browser.find_element(by=By.ID, value='ss')
get_element.send_keys('brasov')
get_element.submit()
button = browser.find_element(by=By.CLASS_NAME, value='sb-searchbox__button')
button.click()


