# Exercício 29

vel= int(input('Digite a velocidade na qual seu carro se encontrava em Km/h:'))
multa= (vel-80)*7
if vel > 80:
    print('Você foi multado. O valor de sua multa é de {}'.format(multa))
else:
    print('Você se encontrava dentro da lei, parabéns.')

