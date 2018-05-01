# Exercício 19
import random

A= input('Um nome:')
B= input('Outro nome:')
C= input('Outro nome:')
D= input('Outro nome:')

E= [A,B,C,D]
random.shuffle(E)

print('A lista de apresentação é:')
print(E)

