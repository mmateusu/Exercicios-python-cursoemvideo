# Exercício 33

n1= float(input('Digite um número:'))
n2= float(input('Digite outro número:'))
n3= float(input('Só mais um:'))

if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n1:
    maior = n3
print('O maior número entre os 3 indicados é {}.'.format(maior))

