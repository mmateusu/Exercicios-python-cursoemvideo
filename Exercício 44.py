# Exercício 44
print('Bom dia! ',end='')
preço= float(input('Qual é o preço do produto? R$'))
print('Qual é a condição de pagamento? '
      '\n Opção (1): Á vista no dinheiro/cheque (10% de desconto) '
      '\n Opção (2) Á vista no cartão (5% de desconto) '
      '\n Opção (3): Em até 2x no cartão (preço padrão) '
      '\n Opção (4): Em 3x ou mais no cartão. (20% de juros) ')
cond= int(input('Digite aqui o código da opção desejada: '))

cheque= preço - (preço* 10)/100
cartao= preço - (preço* 5)/100
cartao2= preço
cartao3= preço + (preço* 20)/100

if cond == 1:
    print('O valor a ser pago é de {}R$'.format(cheque))
elif cond == 2:
    print('O valor a ser pago é de {}R$'.format(cartao))
elif cond == 3:
    print('O valor a ser pago é de {}R$'.format(cartao2))
else:
    print('O valor a ser pago é de {}R$'.format(cartao3))