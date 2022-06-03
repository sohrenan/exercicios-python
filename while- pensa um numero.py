# Este programa gera um número aleatório de 1 a 10 da biblioteca random e solicita ao usuário a dar chutes sobre qual
# valor foi selecionado, caso o usuário não adivinhe, será solicitado novamente até o acerto, ao final, será exibido
# qual número aleatório foi gerado assim como o número de tentativas realizadas até a solução

import random
import time
n = int(random.randrange(0, 11))
c = 0
t = 0

while c == 0:
    t += 1
    q = int(input('Insira seu numero: '))
    print('O COMPUTADOR ESTA PROCESSANDO SEU CHUTE')
    time.sleep(1)
    if q == n:
        c += 1
        print('Parabens, você acertou')
    else:
        print('ERRRRRROUUUUUU, tente novamente')
print('foram necessárias {} tentativas para que voce acertasse'.format(t))
