import itertools

# Se verifica daca 2 stringuri sunt anagrame
#
# def verifica(s, ss):
#     if sorted(s) == sorted(ss):
#         print("Stringurile sunt anagrame.")
#     else:
#         print("Stringurile nu sunt anagrame.")
# s1 = input('introdu stringul 1 ')
# s2 = input('introdu stringul 2 ')
# verifica(s1, s2)


# Eliminarea tuturor duplicatelor

# def my_function(x):
#     return list(dict.fromkeys(x))
# mylist = my_function(['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu'])
# print(mylist)

# mylist2 = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']
# myset = set(mylist2)
# print(myset)


# Sa se verifice daca un string este palindrom

# def palindrom(string):
#     if string[::-1] == string:
#         return 'Stringul este palindrom'
#     return 'Stringul nu este palindrom'
# str_palindrom  = input('introduceti stringul ')
# print(palindrom(str_palindrom))


# Sa se verifice ce numere lipsesc dintr-un interval
# def find_missing(lll):
#     return [x for x in range(lll[0], lll[-1] + 1)
#             if x not in lll]
# lst = [1, 2, 4, 6, 7, 9, 10]
# print(find_missing(lst))


# invers string
# def invers_str(string):
#     rev = string[::-1]
#     return f'inversul stringului  este {rev}'
# str_invers = input('introdu string ')


# permutari

# zzz = input('introdu string')
# lst = [''.join(p) for p in permutations(zzz)]
# print(lst)

# def permutations(string, step=0):
#     if step == len(string):
#         print("".join(string))
#     for i in range(step, len(string)):
#         string_copy = [character for character in string]
#         string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
#         permutations(string_copy, step + 1)
# print(permutations('day'))


def mx_mn(hl):
    mn = hl.split()
    return min(mn) + ' ' + max(mn)


hl = '1 2 3 4 5 6 7 8 -9'
print(mx_mn(hl))
ss = hl.split()
print(ss)

lst = [1, 2, 45, 55, 45, 2, 3, -44, 44, -8, 3, 3]
z = max(lst, key=lst.count)
print(z)
pp = lst.count('iii')
print(pp)



