import math
a = float(input('Informe o Valor do Ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O Seno do Ângulo é: {:.2f}'.format(sen))
print('O Cosseno do Ângulo é: {:.2f}'.format(cos))
print('A Tangente do Ângulo é: {:.2f}'.format(tan))