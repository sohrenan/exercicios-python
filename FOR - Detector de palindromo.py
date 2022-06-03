# Este programa através de um loop FOR analisará se a frase digitada pelo usuário é um palindromo (palavra que escrita
# ao inverso é igual à original) ou não.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('voce digitou a frase: {} ' .format(junto))
for c in range(len(junto)-1, -1, -1):
    inverso += junto[c]

if inverso == junto:
    print('sua frase é palindromo')
else:
    print('sua frase não é palindromo')