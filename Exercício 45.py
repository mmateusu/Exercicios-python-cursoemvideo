# Exercício 45

from random import *
print('Bom dia! ',end='')
eu= input('Vamos jogar! Digite entre pedra, papel ou tesoura: '.lower())
lista= ['pedra', 'papel', 'tesoura']
pc= choice(lista)

if eu == 'pedra' and pc == 'papel':
    print('Você perdeu. O computador escolheu {}.'.format(pc).capitalize())
elif eu == 'papel' and pc == 'tesoura':
    print('Você perdeu. O computador escolheu {}.'.format(pc).capitalize())
elif eu == 'tesoura' and pc == 'pedra':
    print('Você perdeu. O computador escolheu {}.'.format(pc).capitalize())
elif eu == 'papel' and pc == 'pedra':
    print('Você ganhou! O computador escolheu {}.'.format(pc).capitalize())
elif eu == 'tesoura' and pc == 'papel':
    print('Você ganhou! O computador escolheu {}.'.format(pc).capitalize())
elif eu == pc:
    print('Deu empate. O computador também escolheu {}'.format(pc))
elif eu == 'pedra' and pc == 'tesoura':
    print('Você ganhou! O computador escolheu {}.'.format(pc))
print('=== Fim de Jogo ===')