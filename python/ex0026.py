'''frase = str(input('Digite uma frase: ')).strip()
print('Sua frase é {}'.format(frase))
print('Quantidade de letra A é {}'.format(frase.count('a')))
print('Primeira posição da letra A na frase é {}'.format(frase.find('a'.strip())))
print('Ultima posição da letra A na frase é {}'.format(frase.rfind('a'.strip())))'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primiera letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}.'.format(frase.rfind('A')+1))

