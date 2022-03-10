from itertools import permutations
# Scrie un program care sa afiseze toate combinarile de 2 litere dintre valorile dictionarului de mai jos:
dictionar = {"1": "abc", "2": "s", "3": "o", "4": "n", "5": "lm", "6": "jk", "7": "gi", "8": "def", "9": "abc"}


def comb_two(dic):
    left = []
    for k, v in dic.items():
        if len(v) == 2:
            left.append(v)
    r = ''.join(left)
    lst = [''.join(p) for p in permutations(r)]
    return lst


print(comb_two(dictionar))
