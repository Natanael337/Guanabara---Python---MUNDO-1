import random
a1 = input('Digite o Nome do Primeiro Aluno: ')
a2 = input('Digite o Nome do Segundo Aluno: ')
a3 = input('Digite o Nome do Terceiro Aluno: ')
a4 = input('Digite o Nome do Quarto Aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))