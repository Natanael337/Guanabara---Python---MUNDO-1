import math
co = float(input('Informe o Comprimento do Cateto Oposto: '))
ca = float(input('Informe o Comprimento do Cateto Adjacente: '))
h = math.hypot(co, ca)
print('O comprimento da Hipotenusa é: {:.2f}'.format(h))
