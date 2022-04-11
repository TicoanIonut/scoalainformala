import csv
from collections import defaultdict

from numpy import average
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_url(day):
    return f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-ianuarie-ora-13-00/"


browser = webdriver.Chrome(ChromeDriverManager().install())

date = defaultdict(list)
lista_dates = []
for day in range(20, 28):
    lista_dates.append(f'{day}')
    url = get_url(day)
    browser.get(url)
    table = browser.find_element(by=By.XPATH, value="//table[1]")
    rows = table.text.split("\n")
    header = rows[0]

    for idx, row in enumerate(rows[1:], start=1):
        row = row.replace("Satu Mare", "Satu-Mare")
        row = row.replace("Mun. București", "București")

        if idx <= 42:
            nr_crt, judet, cazuri, cazuri_noi, incidenta = row.split(" ")
            if cazuri_noi == '–':
                cazuri_noi = 0

            date[judet].append(
                (
                    int(cazuri.replace(".", "")),
                    int(cazuri_noi),
                    float(incidenta.replace(",", ".")),
                )
            )

lista_cu_randuri_finale = []
for jud, valori in date.items():
    cazuri_confirmate = sum([val[0] for val in valori])
    cazuri_noi = sum([val[1] for val in valori])
    inci = round(average([val[2] for val in valori]), 2)


    lista_cu_randuri_finale.append(
        {
            "Judet": jud,
            "Număr de cazuri confirmate(total) pe 7 zile": cazuri_confirmate,
            "Număr de cazuri nou confirmate pe 7 zile": cazuri_noi,
            "Incidența  înregistrată la 14 zile pe ultimele 7 zile": inci,
        }
    )

with open(r'C:\Users\2dor\PycharmProjects\scoalainformala\teme_curs_09\Covid.csv', 'w', encoding="utf-8") as fp:
    writer = csv.DictWriter(fp, fieldnames=list(lista_cu_randuri_finale[0].keys()))
    writer.writeheader()
    writer.writerows(lista_cu_randuri_finale)
