# Este programa calcula o valor das parcelas e se o financiamento de um imovel hipotético será ou não aprovado
# tendo como critério que o valor da parcela não ultrapasse 30% do salário informado
casa = float(input('Digite o valor do imóvel: '))
salario = float(input('Digite o salário: '))
ano = int(input('Em quantos anos você pretende pagar: '))
meses = ano*12

pm = casa / meses

print('O valor da parcela mensal é de {:.2f}' .format(pm))
if pm <= (salario*0.3):
    print('Seu financiamento FOI aprovado')
else:
    print('Seu financiamento NÃO foi aprovado')


