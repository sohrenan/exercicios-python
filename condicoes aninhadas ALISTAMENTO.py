# Este programa calculará a partir da data de nascimento do usuário sua idade e retornará com a informação sobre o tempo
# que falta ou de atraso para que o mesmo realize o alistamento militar
import time
ano = int(input('digite seu ano de nascimento: '))
year =  int(time.strftime("%Y"))

idade = year - ano
imeses = idade*12
alist = 18*12
tr = alist - imeses

if imeses < alist:
    print('voce tem {:1f} anos portanto não precisa se alistar e faltam {} anos para seu alistamento' .format(idade, tr/12))
elif imeses == alist:
    print('Voce tem {} anos portanto precisa se alistar ESTE ANO ' .format(idade))
else:
    print('Voce tem {} e está {} anos atrasado em seu alistamento' .format(idade, (tr*(-1)/12)))