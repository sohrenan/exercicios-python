# este programa calculará a idade a partir da data de nascimento e retornará em qual categoria de natação o usuário se encaixa.
import time
ano = int(input('digite seu ano de nascimento: '))
year =  int(time.strftime("%Y"))

idade = year - ano
print('sua idade é {}' .format(idade))

if idade <= 9:
    print('Sua categoria é a categoria MIRIM')
elif idade <= 14:
    print('Sua categoria é a categoria INFANTIL')
elif idade <= 19:
    print('Sua categoria é a categoria JUNIOR')
elif idade <= 25:
    print('Sua categoria é a categoria SENIOR')
else:
    print('sua categoria é a MASTER')