import random
n = random.randint(1, 5)
print('Vou pensar em um número entre 1 e 5. Tente adivinhar...')
r = int(input('Em que número eu pensei? '))
if r == n:
    print('Você acertou!')
else:
    print('Você errou! Eu pensei no número {} e não no {}.'.format(n,r))
