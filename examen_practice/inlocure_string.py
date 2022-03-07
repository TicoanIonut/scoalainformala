def nameChanger(x, y, z):
    string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
    # 42 -> 49
    # string = "The Inquisitor must meet Varric on top of Palace's battlements to be introduced."
    # 25 -> 31
    # string = "The Inquisitor must meet King on top of Palace's battlements to be introduced."

    start = string[5:14]
    end = string[26:31]
    text = string[43:49]
    string2 = string.replace(start, x)
    string3 = string2.replace(end, y)
    string4 = string3.replace(text, z)
    #print(string4)
string_value = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
lista = [[5, 14, 'Conquistador'], [26, 31, 'King'], [43, 49, 'Palace']]
for i in sorted(lista, reverse=True):
    #print(i, string_value[i[0]-1:i[1]])
    string_value = string_value.replace(string_value[i[0]-1:i[1]], i[2])
    print(string_value, '>>>')

nameChanger("Conquistador", "King", "Palace")
