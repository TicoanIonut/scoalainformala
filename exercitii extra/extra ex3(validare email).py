import  re
def emailval(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   else:
    return False
s =input('enter email')
if emailval(s)==True:
    print(f'validare {s}')
print(emailval(s))
