# Exercício 41
from datetime import *
nasc= int(input('Qual o ano de nascimento do atleta? ').lstrip())
ano= date.today().year
idade= ano - nasc
if idade <= 9:
    print('A sua categoria é a >Mirim<. Pois possui apenas {} anos.'.format(idade))
elif idade <= 14:
    print('A sua categoria é a >Infantil<. Pois possui {} anos.'.format(idade))
elif idade <= 19:
    print('A sua categoria é a >Junior<. Pois possui {} anos.'.format(idade))
elif idade <= 20:
    print('A sua categoria é a >Sênior<. Pois possui {} anos.'.format(idade))
elif idade > 20:
    print('A sua categoria é a >Master<. Pois possui {} anos.'.format(idade))

