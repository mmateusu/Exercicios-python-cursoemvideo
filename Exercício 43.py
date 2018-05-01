# Exercício 43
from math import *
print('Bom dia! ',end='')
alt= float(input('Digite sua altura: '))
peso= float(input('Digite seu peso: '))
imc= peso / alt**2

if imc < 18.5:
    print('Você está abaixo do peso. Seu IMC é {:.2f}'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal. Seu IMC é {:.2f}'.format(imc))
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso. Seu IMC é {:.2f}'.format(imc))
elif imc > 30 and imc <= 40:
    print('Você está com obesidade. Seu IMC é {:.2f}'.format(imc))
else:
    print('Você está com obesidade mórbida. Seu IMC é {:.2f}'.format(imc))

