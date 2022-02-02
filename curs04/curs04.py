# print('sms')
# format()
# a=input('input date utilizator')
# def functia_mea(param_1):
#     pass
def suma(a,b,c=3):
    """
    :param a: first param
    :param b: second param
    :param c: third param
    :return: sum of params
    """
    return a+b+c
variabila_1 =1
variabila_2 =2
total =suma(variabila_1,variabila_2)
#print(suma(variabila_1,variabila_2)
print(total)
def suma(a:int,b:int,c:int=3)->(int,str):
    """
    :param a: first param
    :param b: second param
    :param c: third param
    :return: sum of params
    """
    return a+b+c,a-b-c
variabila_1 =1
variabila_2 =2
sum,dif =suma(variabila_1,c=0,b=variabila_2)
#print(suma(variabila_1,variabila_2)
print(sum,type(sum))
print(dif,type(dif))
