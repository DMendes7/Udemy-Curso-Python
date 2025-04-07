# https://github.com/luizomf/cursopython2023/blob/main/aula98.py

import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)

print('Fim')
