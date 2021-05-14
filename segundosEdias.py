# Desenvolva utlizando Laços de Repetição

# Escreva um programa em Python que pede ao utilizador que lhe forneça
# um inteiro correspondente a um número de segundos e que calcula o número de dias
# correspondentes a esse número de segundos. O número de dias é fornecido como um
# real. O programa termina quando o utilizador fornece um número negativo. 
# O seu programa deve possibilitar a seguinte interação:

# Escreva um número de segundos (um número negativo para terminar)
# ? 45
# O número de dias correspondente é 0.0005208333333333333
# Escreva um número de segundos (um número negativo para terminar)
# ? 6654441
# O número de dias correspondente é 77.01899305555555
# Escreva um número de segundos (um número negativo para terminar)
# ? -1



diaEmSegundos = 24 * 60 * 60
num_segundos = 0

while ( num_segundos >= 0 ):
  num_segundos = int(input("Escreva um número em segundos: "))
  if (num_segundos < 0):
    break
  num_dias = num_segundos / diaEmSegundos
  print("O número de dias correspondente é ", num_dias)
print("Fim do programa!")