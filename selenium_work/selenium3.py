from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.booking.com")


def browser_function():
    driver_path = "path/to/chromedriver"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.get("https://target_website.com")
    
    
get_element = browser.find_element(by=By.ID, value='ss')
get_element.send_keys('brasov')
get_element.submit()
# with open('Logo.png', 'wb') as file:
# 	file.write(browser.find_element(by=By.CLASS_NAME, value='bui-button__text').screenshot_as_png)
button = browser.find_element(by=By.CLASS_NAME, value='sb-searchbox__button')
button.click()


