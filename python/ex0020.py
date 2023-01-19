'''import random
print('Vamos sortear alunos entre os numeuros 1 e 4.')
lista = input('Nome do aluno1: '), \
input('Nome do aluno2: '), \
input('NOme do aluno3: '), \
input('Nome do aluno4: ')
print(sorted(lista))'''
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação da lista será')
print(lista)



