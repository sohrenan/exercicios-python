# Esta calculadora solicita dois valores que poderão ser somados, multiplicados ou comparados dependendo da seleção
# realizada pelo usuário

c = 0
d = 0

while c == 0:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))

    print('Escolha a operação: ')
    print('''[1]SOMAR
             [2]MULTIPLICAR
             [3]MAIOR
             [4]ESCOLHER NOVOS NUMEROS
             [5]SAIR DO PROGRAMA''')

    e = int(input('Digite sua escolha: '))

    if e == 1:
        print('A SOMA DOS DOIS NUMEROS É {}' .format(n1+n2))
        c += 1
    if e == 2:
        print('A MULTIPLICACAO DOS DOIS NUMEROS É {}'.format(n1 * n2))
        c += 1
    if e == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}'.format(n1,n2))
        elif n2 > n1:
            print('O número {} é maior que o número {}'.format(n2, n1))
        else:
            print('os números {} e {} são iguais' .format(n1, n2))
    c += 1
    if e == 4:
        c = 0
    if e == 5:
        c +=1


print('fim')