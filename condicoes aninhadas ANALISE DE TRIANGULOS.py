# Este programa retorna, através da análise do comprimento dos lados de um triangulo, se é possível formar o triângulo
# e caso sim, qual tipo de triângulo será gerado através das medidas fornecidas.
a = int(input('Digite um número: '))
b = int(input('digite outro número: '))
c = int(input('digite outro número: '))

if (a+b) > c and (a+c) > b and (b+c) > a and a == b and a == c and b == c:
    print('É possível formar um triangulo com os lados {}, {} e {} e o triangulo é EQUILATERO'  .format(a, b, c))
elif (a+b) > c and (a+c) > b and (b+c) > a and a == b and a != c or a == c and a !=b or b == a and b != c or b != a and b == c or c == a and c != b or c == b and c != a :
    print('É possível formar um triangulo com os lados {}, {} e {} e o triangulo é ISOSCELES'  .format(a, b, c))
elif (a+b) > c and (a+c) > b and (b+c) > a and a != b and a != c and b != c:
    print('É possível formar um triangulo com os lados {}, {} e {} e o triangulo é ESCALENO'  .format(a, b, c))
else:
    print('Não é possível formar um triangulo com os lados {}, {} e {}'.format(a, b, c))