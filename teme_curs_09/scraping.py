from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# import pandas as pd

url = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/"
lll = []
for i in range(20, 28):
    z = url.replace('20', str(i))
    lll.append(z)
browser = webdriver.Chrome(ChromeDriverManager().install())
for ele in lll:
    browser.get(ele)
    print(ele)
table = browser.find_element(by=By.XPATH, value='//table[1]')
print(table)
    # table_text = table.text
    # print(table_text)
    # lista = table_text.split('\n')
    # header_len = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]')
    # header = header_len.text.split('\n')
    # dictionar = {i: [] for i in header}
    # for j in range(0, len(header)):
    #     for i in range(len(header) + int(j), len(lista), len(header)):
    #         dictionar[header[int(j)]].append(lista[i])
    # # print(dictionar)
    # df = pd.DataFrame(dictionar)
    # print(df)
    # df.to_csv("Covid.csv")


