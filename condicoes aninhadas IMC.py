# Este programa calcula a partir do peso e altura quando o seu indice de IMC e em qual faixa você se encontra.
p = float(input('Digite seu peso em KG: '))
a = float(input('Digite sua altura em M: '))
imc = p/(a**2)

if imc < 18.5:
    print(' seu imc é de {:.1f} e voce está ABAIXO DO PESO' .format(imc))
elif imc >= 18.5 and imc < 25:
    print('seu imc é {:.1f} e voce está NO PESO IDEAL' .format(imc))
elif imc >= 25 and imc < 30:
    print('seu imc é {:.1f} e voce está COM SOBREPESO' .format(imc))
elif imc >=30 and imc < 40:
    print('seu imc é {:.1f} e voce está com OBESIDADE' .format(imc))
elif imc > 40:
    print('seu imc é {:.1f} e voce est[a com OBESIDADE MORBIDA' .format(imc))
