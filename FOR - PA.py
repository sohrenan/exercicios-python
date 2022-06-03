# Este programa calculará uma PA com inicio e razão fornecidos através de um loop FOR
n = int(input('Digite o primeiro termo de sua PA: '))
r = int(input('Digite a razão de sua PA: '))
for c in range(n, 11, r):
    print(c)