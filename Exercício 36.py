# Exercício 36

print('Bom dia!')
valor = int(input('Qual o valor da casa desejada? R$').strip())
salario= int(input('Desculpe a indelicadeza... Mas, qual o seu salário? R$').strip())
anos= int(input('Em quantos anos pretende pagar? ').strip())
pres= anos*365/30
por= salario*30/100
if pres > por:
    print('Infelizmente seu empréstimo foi negado.')
elif pres < por:
    print('Parabéns! Sua casa nova está a caminho! Seu empréstimo foi aprovado.')
print('Os motivos são: A prestação fica {:.1f}, a porcentagem não pode ser superior a 30% e a sua foi {}%'.format(pres, por))

