# 1. Scrie un program care sa calculeze suma dintre trei numere.
# Daca valorile sunt egale, returnati de trei ori suma acestora.(1 punct)


def tri(z1, z2, z3):
    x = z1 + z2 + z3
    if z1 == z2 and z2 == z3:
        x = (z1 + z2 + z3) *3
        return x
    return x

rez1 = int(input(' introdu nr1 '))
rez2 = int(input(' introdu nr2 '))
rez3 = int(input(' introdu nr3 '))
print(tri(rez1, rez2, rez3))
