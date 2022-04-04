from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()


def browser_function():
    driver_path = "path/to/chromedriver"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.get("https://target_website.com")


# search_element = browser.find_element(by=By.ID, value="card_grid")
# print(search_element.text.split('\n'))
find_element = browser.find_elements(by=By.XPATH, value='//div[contains(@id,"card_grid")]/'
                                                        '/a[contains(@class,"card-v2-title")]')
print(find_element)
