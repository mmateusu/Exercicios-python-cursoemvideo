# Exercício 022

print('x  Leitor de nomes  x')
print('Olá, esse é o leitor de nomes, por favor insira seu nome completo na lacuna abaixo.')
nome= input('Nome Completo:')
maiusculo= nome.upper()
minusculo= nome.lower()
div= nome.split()
tmh= len(nome.strip())
primer= len(div[0])
print('Nome Maiúsculo:{}'.format(maiusculo))
print('Nome Minúsculo:{}'.format(minusculo))
print('Letras ao todo:{}'.format(tmh))
print('Letras do primeiro nome:{}'.format(primer))
