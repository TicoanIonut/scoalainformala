import re

# PRINT ALL '#' IN THE STRING

# inp = '#ASDJAOSDJA&DYH@&IHDJDOJH#&OU#J*O#JM*OJ(OHNIU UHHY *& HY#*^ H*&#Y *&&(*O U(&Y^ITG &%F&#I%^&# &^G #&I^%^ #^&T '
# pat = r'#\w+|#$'
# z = re.findall(pat, inp)
# if z:
#     print('\n'.join(z))
# print(z)

# PHONE NUMBERE VALIDATOR ( must start withi 1 or 8 or 9, must be 8 digit long)

inp = input(">>")
path = r"^[9,8,1]{1,1}[0-9]{7}$"
z = re.match(path, inp)
if z:
    print('Valid')
else:
    print('Invalid')
