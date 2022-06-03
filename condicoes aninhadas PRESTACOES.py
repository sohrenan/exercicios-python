# Este programa calculará o valor cobrado de um produto cujo o preço será informado em 4 formas de pagamento
# sendo que a vista em dinheiro ou cheque retornará o valor com 10% de desconto, a vista no cartão com 5% de desconto,
# parcelado em 2x sem nenhum desconto e parcelado em 3x ou mais com acrescimo de 20%
preco = float(input('Digite o valor do produto: '))

print('''[ 1 ] PARA PAGAMENTO A VISTA EM DINHEIRO OU CHEQUE
[ 2 ] PARA PAGAMENTO A VISTA NO CARTAO
[ 3 ] PARA PAGAMENTO EM 2X NO CARTAO
[ 4 ] PARA PAGAMENTO EM 3X OU MAIS NO CARTAO''')

parc = int(input())

if parc == 1:
    print('VOCE ESCOLHEU O PAGAMENTO A VISTA EM DINHEIRO/CHEQUE')
elif parc == 2:
    print('VOCE ESCOLHEU O PAGAMENTO A VISTA NO CARTAO')
elif parc == 3:
    print('VOCE ESCOLHEU O PAGAMENTO EM 2X NO CARTAO')
elif parc == 4:
    print('VOCE ESCOLHEU O PAGAMENTO EM 3X OU MAIS NO CARTAO')

print('='*100)

if parc == 1:
    print('SEU PRODUTO CUSTA {} MAS COM O DESCONTO O VALOR FICARA EM {} REAIS' .format(preco, preco*0.9))
elif parc ==2:
    print('SEU PRODUTO CUSTA {} E COM O DESCONTO O VALOR FICARA EM {} REAIS' .format(preco, preco*0.95))
elif parc == 3:
    print('SEU PRODUTO CUSTA {} E O VALOR FICARA EM {} REAIS' .format(preco, preco))
elif parc == 4:
    print('SEU PRODUTO CUSTA {} E O VALOR FICARA EM {} REAIS' .format(preco, preco*1.2))
print('='*100)
print('OBRIGADO PELA PREFERENCIA E VOLTE SEMPRE')