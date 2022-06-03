# Este programa realizará a leitura de 6 valores e retornará quantos foram inteiros e a soma dos valores inteiros fornecidos.
s = 0
cont = 0
for c in range (1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        cont += 1

print('Houveram {} valores compativeis e o somatorio de todos os valores foi {}' .format(cont, s))

