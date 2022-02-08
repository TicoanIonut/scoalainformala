# import  re
# def emailval(s):
#    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
#    if re.match(pat,s):
#       return True
#    else:
#     return False
# mmm =input('enter email')
# if emailval(mmm)==True:
#     v=mmm.split('@')
#     print(f'validare reusira @{v[1]}')

def mal(mail):
    cifnr=mail.split('@')
    cifnr1=mail.split('.')
    if cifnr[0] is type(1) or type('s'):
        if cifnr1[0] is type(1) or type('s'):
            if cifnr1[1] is not type(1):
                return True
    else:
        return False
mmm=input('enter mail')
if mal(mmm) == True:
    v=mmm.split('@')
    print(f'validare reusita @{v[1]}')