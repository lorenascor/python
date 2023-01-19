'''nome = str(input('Digite o seu Nome completo? '))
lista = nome.split()
print('Seu Nome completo é {}'.format(nome))
print(lista[:1])
print(lista[-1:])'''
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('É um prazer te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))






