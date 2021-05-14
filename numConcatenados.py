# Desenvolva utlizando Laços de Repetição

# Escreva um programa em Python que lê uma sequência de dígitos, sendo
# cada um dos dígitos fornecido numa linha separada, e calcula o número inteiro composto
# por esses dígitos, pela ordem fornecida. Para terminar a sequência de dígitos é fornecido
# ao programa o inteiro −1. Por exemplo, lendo os dígitos 1 5 4 5 8, o programa calcula o
# número inteiro 15458.


num_concatenados = ''

while True:
    numero = int(input("Escreva um número inteiro: "))
    if numero == -1:
        break
    num_concatenados = num_concatenados + str(numero)
print("O número inteiro é: ", num_concatenados)