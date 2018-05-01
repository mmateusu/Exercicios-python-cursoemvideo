# Exercício 42
print('Bom dia!')
a= int(input('Digite um dos lados do triângulo: '))
b= int(input('Digite outro lado: '))
c= int(input('Digite mais um apenas: '))

if b-c < a and a < b+c and a-c < b and b < a+c and a-b < c and c < a+b:
    print('O triângulo é possível sim! ', end='')
    if a == b == c:
        print('E digo mais: Esse triângulo é Equilátero!')
    elif a != b and b != c and a != c:
        print('E digo mais: Esse triângulo é Escaleno!')
    elif a == b or b == c or a == c:
        print('E digo mais: Esse triângulo é Isósceles!')
else:
    print('Não é possível não...')
