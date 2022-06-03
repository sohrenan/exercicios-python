# este programa irá ler 5 pesos através de um loop FOR e retornará o maior e o menor peso fornecidos pelo usuário
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite seu peso em KG: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi {} e o menor {}' .format(maior, menor))

