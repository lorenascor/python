'''nome = str(input('Nome completo: '))
print('Seu nome em letra maisculas {}'.format(nome.upper()))
print('Seu nome em letra minusculas {}'.format(nome.lower()))
print('Seu nome tem {} cararectes'.format(len(nome.strip())))
primeiro = nome.split()
print('Seu primeiro nome é {}'.format(primeiro[0]))'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))



