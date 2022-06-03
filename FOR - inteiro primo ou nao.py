# Este programa através de um loop FOR retornará se um número é primo ou não.
n = int(input('Digite um número: '))
tot = 0
for c in range(1,n+1):
    if n % c == 0:
        tot += 1
if tot == 2:
            print('o número é primo')
else:
            print('o numero nao é primo')



