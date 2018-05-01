# Exercício 38
print('Bom dia!')
n1= int(input('Digite um número inteiro: '))
n2= int(input('Digite outro número inteiro:'))
if n1>n2:
    print('Entre {} e {} o maior número é {}.'.format(n1, n2, n1))
elif n1==n2:
    print('Não existe número maior, ambos {} e {} são iguais.'.format(n1, n2))
elif n1<n2:
    print('Entre {} e {} o maior número é {}.'.format(n1, n2, n2))
