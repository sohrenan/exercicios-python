## Este programa procede com a soma de números menores que 999
## Caso o valor seja maior que 999, é realizada a soma de todos os valores fornecidos e quantos números
## foram fornecidos até o input 999
n = 0
soma = 0
c = 0
d = 1

while d == 1:
    n = int(input('Digite um numero: '))
    if n < 999:
        soma += n
        c +=1
    else:
        d = 0

print('A soma dos valores é {} e foram digitados {} numeros' .format(soma, c))
