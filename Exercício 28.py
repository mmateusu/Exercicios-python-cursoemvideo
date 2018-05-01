# Exercício 28
from random import *

num= int(input('Olá! Esse é o jogo "advinhe o que estou pensando". Digite um valor no qual você acha que eu estou pensando (Tem que ser de 0 á 5 ein!):'))
pc= randint(0,5)

if pc== num:
    print('Parabéns você ganhou. O numero que eu pensei foi {} e você digitou {}'.format(pc,num))
else:
    print('Uh, você errou. O número que eu pensei foi {} e você digitou {}'.format(pc,num))
