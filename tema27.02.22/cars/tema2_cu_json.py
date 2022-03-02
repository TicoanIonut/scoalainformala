import pandas as pd
import os


def fisier_inp():
    lista_masini = {
      "masina1": {"id": "random", "brand": "Ford", "model": "Fiesta", "hp": "100", "price": "900"},
      "masina2": {"id": "random", "brand": "Dacia", "model": "Spring", "hp": "110", "price": "990"},
      "masina3": {"id": "random", "brand": "Ford", "model": "Ka", "hp": "60", "price": "800"},
      "masina4": {"id": "random", "brand": "Renault", "model": "Clio", "hp": "90", "price": "990"},
      "masina5": {"id": "random", "brand": "VW", "model": "up", "hp": "66", "price": "975"},
      "masina6": {"id": "random", "brand": "Ford", "model": "Galaxy", "hp": "100", "price": "1500"},
      "masina7": {"id": "random", "brand": "Renault", "model": "Megane", "hp": "120", "price": "2000"},
      "masina8": {"id": "random", "brand": "VW", "model": "Polo", "hp": "120", "price": "1500"},
      "masina9": {"id": "random", "brand": "Audi", "model": "A3", "hp": "140", "price": "2500"},
      "masina10": {"id": "random", "brand": "Nissan", "model": "Juke", "hp": "105", "price": "2000"},
      "masina11": {"id": "random", "brand": "Audi", "model": "A8", "hp": "250", "price": "7000"},
      "masina12": {"id": "random", "brand": "Dacia", "model": "Duster", "hp": "120", "price": "1500"},
      "masina13": {"id": "random", "brand": "Nissan", "model": "GTR", "hp": "900", "price": "7500"},
      "masina14": {"id": "random", "brand": "VW",  "model": "T6", "hp": "130", "price": "3500"},
      "masina15": {"id": "random", "brand": "Audi", "model": "A6", "hp": "200", "price": "3000"}
    }
    for d in lista_masini.values():
        d['id'] = d['brand'][0] + d['model'][0] + d['hp'][0] + d['price'][0]
    df = pd.DataFrame(lista_masini)
    df.to_csv('input.csv')


def make_folder():
    directory = 'output_data'
    parent_dir = r"C:\Users\2dor\PycharmProjects\scoalainformala\tema27.02.22\cars"
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
    except OSError:
        pass


def data_frame():
    fisier_inp()
    df = pd.read_csv('input.csv')
    df = df.T                                                                       # swap lista
    df = pd.DataFrame(df.values, columns=["id", "brand", "model", "hp", "price"])   # lista frumoasa
    df = df.drop(df.index[0])                                                       # drop ce nu imi trebuie
    df.hp = pd.to_numeric(df.hp)
    df.price = pd.to_numeric(df.price)                                            # numere ordonate frumos
    make_folder()
    slow_cars = df[df.hp < 120]
    slow_cars.to_json(r'output_data\slow_cars.json')
    fast_cars = df[(df.hp >= 120) & (df.hp < 180)]
    fast_cars.to_json(r'output_data\fast_cars.json')
    sport_cars = df[df.hp >= 180]
    sport_cars.to_json(r'output_data\sport_cars.json')
    cheap_cars = df[df.price < 1000]
    cheap_cars.to_json(r'output_data\cheap_cars.json')
    medium_cars = df[(df.price >= 1000) & (df.hp < 5000)]
    medium_cars.to_json(r'output_data\medium_cars.json')
    expensive_cars = df[df.price >= 5000]
    expensive_cars.to_json(r'output_data\expensive_cars.json')
    df = df.sort_values(by='brand')
    print(df['brand'])
    iii = input('Introdu un filtru\n> ').capitalize()
    filt = df['brand'].str.startswith(iii)
    ps = df.loc[filt]
    ps.to_json(r'output_data\specific_brand.json')
    print(ps)


if __name__ == '__main__':
    data_frame()
