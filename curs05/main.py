# #print()#str
# #input()#str
# #"".format()#str
# def functie2():
#     my_function()
# def my_function():
#     #function body
#     #return None
#     pass
# print(functie2())
# def message():
#     print('enter a value')
# def your_function(name):
#     print('hello',name)
#     return name
# name=input('numele meu este: ')
# your_function(name)
# def my_function(a:str,b:str,c:str='2'):
#     return a,b,c
# # print(my_function(a='1',c='2',b='3'))
# #print(my_function('1',c='2',b='3'))
# #print(my_function('3',a='1',c='2'))
# #print(my_function('1','3',c='2',d='4'))
# print(my_function('1','3','4'))
# def my_function():
#     pass
# a=my_function()
# print(a)
# b=None
# print(type(b))
# def my_func(n:int)->bool:
#     if n%2==0:
#         return True
#     return False
# #print(my_func(3))
# nr=input('introdu un nr:')
# if my_func((int(nr))) is True:
#     print('nr este divizibil')
# elif my_func(int(nr)) is False:
#     print('nr nu este divizibil')
# var=2
# def my_func(var1):
#     global var
#     var=var1
#     return f"cuosti acesata variabila: {var}"
# print(my_func(3))
# var=1
# print(var)
# lista=[1,2,3,[4,5,[6,7]]]
# print(lista[3][2][0])
#try:
    #bloc de expresii
#except:
    #daca apre o exceptie si vrem sa afisam ceva
try:
    val=int(input('prima cifra cnp'))
    #impartire =1/val
    lista=[1]
    #lista.append('2')
    valoare = lista[0.5]
except TypeError:
    print('tip de eroare')
except AttributeError:
    print('eroare la atribut')
except ValueError:
    print('intodu o cifra')
except ZeroDivisionError:
    print('eroare la impartire')
except Exception as e:
    print('exceptie la impartire',e)










