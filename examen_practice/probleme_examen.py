# PROBLEME

# minim si maxim dintr-o lista de numere

# def max_min_func(Lista = []):
#     if len(Lista) < 1:
#         print("lista trebuie sa aiba minim un element")
#     else:
#         high = max(Lista)
#         low = min(Lista)
#         print(f"Maximul din lista este {high}, iar minimul {low}")
#
# max_min_func([1, 2, 3, 4, 5])
# max_min_func([])
# max_min_func([1, 2, -3, 4, 5])
# max_min_func([1, 9, 3, 4, -5])


# import collections
#
# # Se da lista de nume:
#
# lista_nume = ["Maria", "Irina", "Claudiu", "Ionut", "Irina", "Matei", "Irina", "Maria", "Claudiu"]
#
# # Se cere:
# # 1. Sortati lista dupa nume
#
# def sortare_nume(lista):
#     lista.sort()
#     print(lista)
#
# sortare_nume(lista_nume)
#
#
# # 2. Determinati numarul de aparitii al fiecarui nume
#
# def nr_aparitie_fiecare(lista):
#     nume = collections.Counter(lista)
#     print(nume)
#
# nr_aparitie_fiecare(lista_nume)
#
# # 3. Listati numele care apare de cele mai multe ori in lista initiala.
#
# def max_aparitii(lista):
#     nume = collections.Counter(lista)
#     lista1 = dict(nume)
#     valori = list(lista1.values())
#     maxim = max(valori)
#     found_key = [key for key, value in lista1.items() if value == maxim]
#     print(found_key)
#
# max_aparitii(lista_nume)
#
# # 4. Listati numele care apare de cele mai putine ori in lista initiala.
#
# def min_aparitii(lista):
#     nume = collections.Counter(lista)
#     lista1 = dict(nume)
#     valori = list(lista1.values())
#     minim = min(valori)
#     found_key = [key for key, value in lista1.items() if value == minim]
#     print(found_key)
#
# min_aparitii(lista_nume)


# Realizati o functie care sa inlocuiasca textul din variabila string
# aflat intre valorile "start" si "end" cu textul din "text".
# [start, end, text]

import itertools


def grouper(n, it):
    it = iter(it)
    return iter(lambda: list(itertools.islice(it, n)), [])


string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."


def replace_text(string_text):
    global new_string
    raspuns_utilizator = input("Doresti sa introduci un patche? (yes/no) ")
    my_list = []
    while raspuns_utilizator != "no":
        start = int(input("Introduceti indexul de start: "))
        if start >= len(string_text):
            print("Indexul de start este prea mare!")
            break
        my_list.append(start)

        end = int(input("Introduceti indexul de end: "))
        if end >= len(string_text):
            print("Indexul de end este prea mare!")
            break
        elif end < start:
            print("Index-ul de end mai mic decat cel de start!")
            break
        my_list.append(end)

        text = input("Introduceti textul care va fi inlocuit: ")
        my_list.append(text)

        raspuns_utilizator = input("Doresti sa introduci un nou patche? (yes/no) ")

        patches = list(grouper(3, my_list))
        print(patches)

        for i in patches:
            sublist = i
            start = sublist[0]
            end = sublist[1]
            text = sublist[2]

            new_string = string_text.replace(string_text[start - 1: end], text)
        string_text = new_string
        print(string_text)


replace_text(string)

# testul initial este: = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# patches = [[5, 14, 'Conquistador'], [28, 33, 'King'], [43, 49, 'Palace']]
# textul rezultat este:   The Conquistador must meet King on top of Palace's battlements to be introduced.
