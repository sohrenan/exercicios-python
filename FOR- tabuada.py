# Este programa retorna a tabuada do valor digitado 
n = int(input('Digite um número: '))

for c in range (0,11):
    print('{} x {} = {}'.format(n, c, n*c))


