import json
import csv

with open('input.csv', 'w') as fisier:
    old_cars = []
    for linie in fisier:
        tokens = linie.strip('\n').split(',')

        categorie = tokens[5].strip()

        if categorie == 'old':
            old_cars.append(tokens)
            print(categorie)

    with open('old_cars.json', 'w') as old_cars_fisier:
        json.dump(old_cars, old_cars_fisier)
