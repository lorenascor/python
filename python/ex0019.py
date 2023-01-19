'''import random
print('Vamos sortear alunos entre os numeuros 1 e 4.')
lista = input('Nome do aluno1: '), \
input('Nome do aluno2: '), \
input('NOme do aluno3: '), \
input('Nome do aluno4: ')
print('A lista com os nomes dos alunos é {}. O aluno sorteado foi {}'.format(lista, random.choice(lista)))'''
from random import choice
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
