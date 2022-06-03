# este programa solicitará nome, idade e sexo de duas pessoas distintas através de um loop FOR e retornará
# a informação da média de idades, quem é o homem mais velho e quantas mulheres menores de 20 anos foram registrados.
soma = 0
maisvelho = 0
nomevelho = ''
menosvinte = 0

for c in range(1,3):
    print(' ----- {}º PESSOA ----' .format(c))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    if c == 1 and sexo == 'M' or sexo == "MASCULINO":
        maisvelho = idade
        nomevelho = nome
    else:
        if maisvelho < idade and sexo == 'M' or sexo == "MASCULINO":
            maisvelho = idade
            nomevelho = nome
    if idade <= 20 and sexo == 'F' or sexo == "FEMININO":
        menosvinte += 1



    soma += idade
media = soma / 4

print('''A media de idade do grupo é de {} anos
O nome do homem mais velho é {} 
e o grupo possui {} mulheres com menos de 20 anos''' .format(media, nomevelho, menosvinte))
