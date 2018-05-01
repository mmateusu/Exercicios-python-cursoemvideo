# Exercício 39
from datetime import *
print('Bom dia!')
n1= int(input('Qual o ano do seu nascimento? '))
ano= date.today().year
idade= ano - n1
if idade > 18:
    saldo= idade - 18
    y= ano - saldo
    print('Você já deveria ter se alistado há {} anos atrás, no ano de {}. Corre pra ver isso!'.format(saldo, y))
elif idade == 18:
    print('CORRE!!!! Tá na hora de se alistar irmãozinho!')
elif idade < 18:
    saldo= 18 - idade
    y = ano + saldo
    print('Faltam {} anos pro seu alistamento ainda. Fica tranquilo que é só em {}.'.format(saldo, y))