
import pandas as pd


# def delet():
#     rd = pd.read_csv('task.csv', header=None)
#     print(rd)
#     try:
#         dele = int(input('\n'
#                          'Scrie o cifra conform indexului pe care vrei sa il stergi\n'
#                          '>>'))
#         if dele in range(len(rd.index + 1)):
#             rd = rd.drop(rd.index[dele])
#             print(rd)
#         else:
#             delet()
#     except ValueError:
#         delet()


def chan():
    rz = pd.read_csv('task.csv', header=None)
    print(rz)
    try:
        change = int(input('\n'
                             'Scrie o cifra conform indexului pe care vrei sa il modifici\n'
                             '>>'))
        if change in range(len(rz.index + 1)):
            rz = rz.drop(rz.index[change])
            # rz[filt]['0'] = input('introdu task')
            # rz = rz.loc(rz.index[change])
            print(rz)
        else:
            chan()
    except ValueError:
        chan()


chan()
