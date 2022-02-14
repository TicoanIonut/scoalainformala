import re
import datetime
an='123456789'
cnp=input('enterCNP:')
cnpc= ((2 * cnp[0]) + (7 * cnp[1]) + (9 * cnp[2]) + (1 * cnp[3]) + (4 * cnp[4]) + (6 * cnp[5]) +
          (3 * cnp[6]) + (5 * cnp[7]) + (8 * cnp[8]) + (2 * cnp[9]) + (7 * cnp[10]) + (9 * cnp[11]))
#rest=(sum([int(i) for i in cnpc]))%11
rest=sum(map(int,cnpc))%11
date= cnp[1:7]
intcnp=int(cnp[-1])
jud=['01','02','03','04','05','06','07','08','09','10','11','12','13'
    ,'14','15','16','17','18','19','20','21','22','23','24','25','26'
    ,'27','28','29','30','31','32','33','34','35','36','37','38','39'
    ,'40','41','42','43','44','45','46','47','48','49','51','51','52']
#valid ="^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$"
#cu regex functionaza bine cu toate, in afara de data
def cnpval():
    try:
        if datetime.datetime.strptime(date,"%y%m%d"):
            if len(cnp) == 13:
                if cnp[0] in an:
                    if cnp[7:9] in jud:
                        if intcnp == rest:
                            return True
    except:
        return False
if cnpval()==True:
     print(f'CNP Valid: {cnp}')
else:
    print('CNP invalid, mai incearca')