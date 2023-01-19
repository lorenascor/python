cidade = str(input('Digite o nome cidade? ')).strip()
print('Nome da cidade é {}'.format(cidade))
print('Nome da cidade começa com Santo Verdadeiro ou Falso?'.format(cidade))
print(cidade[:5].upper() == 'SANTO')

