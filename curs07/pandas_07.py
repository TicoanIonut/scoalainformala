import pandas as pd
import json

# dictionar_date = {
#     "masini": ['dacia', 'volvo', 'renault'],
#     "culoare": ['rosu', 'alb', 'verde']
# }
# variabila =pd.DataFrame(dictionar_date)
# print(variabila)

# masini = ['dacia', 'volvo', 'renault']
# variabila = pd.Series(masini, index=['x', 'y', 'z'])
# # print(variabila[0])
# print(variabila['y'])
# print(variabila)

# masini = {'x': 'dacia', 'y': 'volvo', 'z': 'renaut'}
# variabila = pd.Series(masini)
# print(variabila)

# dictionar_date = {
#     "masini": ['dacia', 'volvo', 'renault'],
#     "culoare": ['rosu', 'alb', 'verde']
# }
# variabila = pd.DataFrame(dictionar_date, index = ['producator1', 'producator2', 'producator3'])
# print(variabila.loc[0])
# print(variabila.loc[[0, 1]])
# print(variabila.loc[['prod1', 'prod2']])
data = {
  "producator1": {
    "masini": "dacia",
    "culoare": "rosu"
  },
  "producator2": {
    "masina": "volvo",
    "culoare": "alb"
  },
  "producator3": {
    "masina": "renault",
    "culoare": "verde"
  }
}
variabila1 = pd.DataFrame(data)
# variabila1 = pd.read_json('data.json')
# print(variabila1)
# url = 'https://api.exchangerate-api.com/v4/latest/USD'
# var1 = pd.read_json(url)
# print(var1)
fisier = variabila1.to_csv("data.csv")





