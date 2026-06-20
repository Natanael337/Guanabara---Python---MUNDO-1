l = float(input('Digite a Largura da Parede: '))
a = float(input('Digite a Altura da Parede: '))
ar = l * a
t = ar / 2
print('Sua parede tem: {:.2f} metros quadrados e será necessário {:.2f} litros de tinta'.format(ar, t))
