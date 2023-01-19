from math import hypot
co = float(input('Qual é o valor do cateto oposto? '))
ca = float(input('Qual é o valor do cateto adjacente? '))
'''hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
print('O valor do cateto oposto {} e o valor do cateto adjacente é {} é igual a hipotenusa {:.2f}'.format(co,ca, hipotenusa))'''
hi = hypot(co, ca)
print('O valor da hipotenusa {:.2f}'.format(hi))

