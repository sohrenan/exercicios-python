### Calculadora de média de vários números
## Criado um loop While para que seja possível repetir inputs de valores que se deseja calcular
## ao fim dos inputs,  há o retorno do calculo de qual o maior valor digitado, menor valor digitado e a média entre eles

c = soma = maior = menor = media = resultado =0
d = 1
while d == 1:
    n = int(input('digite um valor: '))
    soma += n
    resultado = soma
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    escolha = str(input(('deseja digitar mais algum valor? [S/N]'))).upper()
    if escolha == 'S':
        d == 1
    else:
        d += 2
media = resultado / c
print('''a média entre os numeros é {} e 
o maior número é {} e
o MENOR numero é {}'''.format(media, maior, menor))







