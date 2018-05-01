# Exercício 31

km= float(input('Pra onde você vai viajar? Digite a distância em KM/H:'))
p200= km*0.50
p300= km*0.45

if km < 200:
    print('Já que você vai viajar menos que 200 Km o preço é R$0,50 por Km. Fica R${:.2f}'.format(p200))
else:
    print('Opa, se vai viajar isso tudo eu faço um desconto, R$0,45 por KM. Fica R${:.2f}'.format(p300))