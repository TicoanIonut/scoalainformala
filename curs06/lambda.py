# my_lambda = lambda x, y: x+y
# #denumire_functie = lambda param1, param2: corp functie
# my_sum =my_lambda(2, 3)
# print(my_sum)
#
#
# def my_lambda(x, y):
#     return x + y


# diferenta = lambda x, y, z: z - y
# dif = diferenta(4, 3, 5)
# print(dif)

players = [{
    "first_name": "Ion",
    "last_name": "Gheorghe",
    "varsta": 12
    }
    ,{
        "first_name": "andreea",
      "last_name": "popa",
      'varsta': 35
    },
    {
        "first_name": "Isabela",
      "last_name": "enache",
      'varsta': 25
    }]

jucatori_sortati = sorted(players, key=lambda jucator: jucator['varsta'])
print(jucatori_sortati)