#Este programa calculará uma PA a partir do número fornecido e a razão fornecida, fornecendo a opção de
# exibir mais termos caso seja solicitado
n = int(input('Digite o primeiro numero de sua PA: '))
r = int(input('Digite a razão de sua PA: '))
pa = n
c = 0
resultado = 0


while c < 10:
    pa += r
    c += 1
    resultado = pa
    print(pa)
print('VOCE GOSTARIA DE EXIBIR MAIS TERMOS? [S/N]')
escolha = str(input(' ')).upper()
if escolha == 'S':
    termos = int(input('DIGITE QUANTOS TERMOS ADICIONAIS VOCE GOSTARIA DE EXIBIR'))
    if termos != 0:
        while c < 10 + termos:
            resultado += r
            c += 1
            print(resultado)
    else:
        print('fim')
if escolha == 'N':
    print('fim')

