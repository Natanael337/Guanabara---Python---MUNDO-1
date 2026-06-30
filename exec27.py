n1 = int(input('Digite a Primeira Nota: '))
n2 = int(input('Digite a Segunda Nota '))
m = (n1 + n2) / 2
print('Média: {}'.format(m))
if m > 6:
    print('Aluno Aprovado!')
else:
    print('Aluno Reprovado!')
