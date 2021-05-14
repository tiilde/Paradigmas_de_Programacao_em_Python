# Desenvolva utilizando LISTAS.

# Crie um programa que leia números inteiros do usuário até que uma
# linha em branco seja inserida. Uma vez que todos os números inteiros foram lidos, seu
# programa deve exibir todos os números, seguidos por todos os zeros, seguidos por
# todos os números positivos.
# Dentro de cada grupo, os números devem ser exibidos na mesma ordem em que foram
# inseridos pelo usuário.
# Por exemplo, se o usuário digitar os valores 3, -4, 1, 0, -1, 0 e -2,
# Então seu programa deve gerar os valores -4, -1, -2, 0, 0, 3 e 1.

# OBS: Seu programa deve exibir cada valor em sua própria linha.



lista_int = []

# Entrada de números inteiros
while True:
    num = input("Digite um número inteiro: ")

    if num == '':
        break

    lista_int.append(int(num))
    print(lista_int)

# lista_int = [3, -4, 1, 0, -1, 0,-2]

# Criando lista de numeros digitados
lista_int_negativos = []
lista_int_zeros = []
lista_int_positivos = []
for numero_int in lista_int:
    if numero_int < 0:
        lista_int_negativos.append(numero_int)
    elif numero_int == 0:
        lista_int_zeros.append(numero_int)
    else:
        lista_int_positivos.append(numero_int)

# Exibindo números na ordem
for numero_int_negativo in lista_int_negativos:
    print(numero_int_negativo)

for numero_int_zero in lista_int_zeros:
    print(numero_int_zero)

for numero_int_positivo in lista_int_positivos:
    print(numero_int_positivo)