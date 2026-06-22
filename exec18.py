import random
a1 = input('Digite o Nome do Primeiro Aluno: ')
a2 = input('Digite o Nome do Segundo Aluno: ')
a3 = input('Digite o Nome do Terceiro Aluno: ')
a4 = input('Digite o Nome do Quarto Aluno: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))