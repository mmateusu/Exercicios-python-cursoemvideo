# Exercício 40

n1= float(input('Digite sua primeira nota: '))
n2= float(input('Digite sua segunda nota: '))
m= (n1 + n2) / 2

if m < 5:
    print('Infelizmente você foi reprovado. Sua média foi de {}'.format(m))
elif m >= 5 and  m < 6.9:
    print('Olha, você está de recuperação. Sua média foi de {}.'.format(m))
elif m > 6.9:
    print('Parabéns, você passou! Sua média foi de {}!'.format(m))
