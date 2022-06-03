# Este programa simula um jogo de pedra, papel e tesoura utilizando condicionais aninhadas.
import random
import time
print('='*100)
print('''[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
print('='*100)
n = int(input('Digite sua escolha: '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)
print('='*100)
c = random.randrange(1,3)

if n == 1 and c == 1:
    print('Voce escolheu PEDRA e o computador escolheu PEDRA, VOCES EMPATARAM')
elif n == 1 and c == 2:
    print('Voce escolheu PEDRA e o computador escolheu PAPEL, COMPUTADOR GANHOU')
elif n == 1 and c == 3:
    print('Voce escolheu PEDRA e o computador escolheu TESOURA, VOCE GANHOU')
elif n == 2 and c == 1:
    print('Voce escolheu PAPEL e o computador escolheu PEDRA, VOCE GANHOU')
elif n == 2 and c == 2:
    print('Voce escolheu PAPEL e o computador escolheu PAPEL, VOCES EMPATARAM')
elif n == 2 and c == 3:
    print('Voce escolheu PAPEL e o computador escolheu TESOURA, COMPUTADOR GANHOU')
elif n == 3 and c == 1:
    print('Voce escolheu TESOURA e o computador escolheu PEDRA, COMPUTADOR GANHOU')
elif n == 3 and c == 2:
    print('Voce escolheu TESOURA e o computador escolheu PAPEL, VOCE GANHOU')
elif n == 3 and c == 3:
    print('Voce escolheu TESOURA e o computador escolheu TESOURA, VOCES EMPATARAM')
print('='*100)
print('OBRIGADO POR JOGAR')
print('='*100)