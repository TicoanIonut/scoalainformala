import  re
def emailval(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   else:
    return False
mmm =input('enter email')
if emailval(mmm)==True:
    v=mmm.split('@')
    print(f'validare reusira @{v[1]}')