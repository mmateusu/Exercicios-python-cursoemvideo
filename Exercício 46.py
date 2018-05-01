from time import *
from emoji import *

print('A contagem regressiva para os fogos começou: ')
for c in range(10,-1,-1):
    sleep(1)
    print(c)
print(emojize('BOOM! :boom:', use_aliases=True))
