# Exercício 34

sal= float(input('Digite o valor do seu salário em R$:'))
if sal > 1250:
    sal= sal+(sal*10/100)
if sal <= 1250:
    sal= sal+(sal*15/100)
print('Seu salário passará a ser: R${}'.format(sal))