# Desenvolva utilizando LISTAS.

# Neste exercício, você criará um programa que lê palavras do usuário até
# que o usuário entre com uma linha em branco. Após o usuário digitar uma linha em
# branco, seu programa deve exibir cada palavra inserida pelo usuário exatamente uma
# vez. As palavras devem ser exibidas em na mesma ordem em que foram inseridos. Por
# exemplo, se o usuário digitar:

# primeiro
# segundo
# primeiro
# terceiro
# segundo

# então seu programa deve exibir:
# primeiro
# segundo
# terceiro


lista_palavra = []
condicao = True
while condicao:
    p = input("Escreva uma palavra: ")
    if p == '':
        condicao = False
    else:
         lista_palavra.append(p)
         
lista_exclusao = []
for i in range (len(lista_palavra)):
    if lista_palavra[i] not in lista_exclusao:
        lista_exclusao.append(lista_palavra[i])
        print(lista_palavra[i])