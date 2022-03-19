import re

# PRINT ALL '#' IN THE STRING

# inp = '#ASDJAOSDJA&DYH@&IHDJDOJH#&OU#J*O#JM*OJ(OHNIU UHHY *& HY#*^ H*&#Y *&&(*O U(&Y^ITG &%F&#I%^&# &^G #&I^%^ #^&T '
# pat = r'#\w+|#$'
# z = re.findall(pat, inp)
# if z:
#     print('\n'.join(z))
# print(z)

# PHONE NUMBERE VALIDATOR ( must start withi 1 or 8 or 9, must be 8 digit long)

# inp = input(">>")
# path = r"^[9,8,1]{1,1}[0-9]{7}$"
# z = re.match(path, inp)
# if z:
#     print('Valid')
# else:
#     print('Invalid')

path = r'(0[1-9]|1[0-9]|2[0-9]|3[0-9]|4[06]|5[1-2])'
inp = input(">>")
# path = r'(!47|48|49|50)[0-4][1-9]|51|52'
z = re.match(path, inp)
if z:
    print('Valid')
else:
    print('Invalid')
