# Este programa calcula a média do estudante a partir da pontuação de duas provas e retorna se o mesmo foi aprovado, está de recuperação ou foi reprovado.
n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda provaa: '))
m = (n1+n2)/2

if m < 5:
    print('sua média foi {} e voce foi REPROVADO' .format(m))
elif 5 <= m <= 6.9:
    print(' sua média foi {} e voce está de RECUPERAÇAO' .format(m))
else:
    print('sua média foi {} e voce está APROVADO' .format(m))

