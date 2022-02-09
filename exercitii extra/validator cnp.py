import re
import mmap
import random
def cnpval(s):
    valid ="^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$"
    if re.match(valid,s):
        if s[0]==random.randint(0,9):
            if datetime.s[1:6]:
                print('sss')
    else:
         return False

cnp=input('enterCNP:')
if cnpval(cnp)==True:
     print(f'CNP Valid: {cnp}')


