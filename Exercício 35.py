# Exercício 35

a= int(input('Digite um dos lados do triângulo:'))
b= int(input('Mais um:'))
c= int(input('Ultima vez:'))

if b-c < a and a < b+c and a-c < b and b < a+c and a-b < c and c < a+b:
    print('É possível sim!')
else:
    print('Infelizmente não é possível construir esse triângulo.')