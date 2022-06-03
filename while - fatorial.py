# Este programa realiza o calculo do fatorial do número fornecido através do loop while

n = int(input('DIGITE UM NUMERO PARA CALCULAR O FATORIAL: '))
g = n
f = (n-1)
fatorial = 0

while f != 0:
    n = n*f
    f -= 1
    fatorial = n

print('O valor do fatorial de {} é {}' .format(g, fatorial))



