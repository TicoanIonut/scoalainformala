# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import pandas as pd
#
#
# def browser_function():
#     driver_path = "path/to/chromedriver"
#     chr_options = Options()
#     chr_options.add_experimental_option("detach", True)
#     chr_driver = webdriver.Chrome(driver_path, options=chr_options)
#     chr_driver.get("https://target_website.com")
#
#
# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/')
# get_element = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody')
# afisare = get_element.text
# lista = afisare.split('\n')
# print(lista)
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
table = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody')
table_text = table.text
lista = table_text.split('\n')
header_len = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]')
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])
# print(dictionar)
df = pd.DataFrame(dictionar)
print(df)
df.to_csv("Covid.csv")


