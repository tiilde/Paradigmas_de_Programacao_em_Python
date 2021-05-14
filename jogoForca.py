# Criar o “JOGO DA FORCA”:

# a) Criar uma lista de palavras para o jogo.
# b) O jogo pergunta um número e assim é escolhido a palavra pelo índice.
# c) Utilize uma lista de strings para desenhar o boneco da forca. Assim fica
# mais fácil caso o jogador erre para controlar cada parte.
# d) Apresentar a palavra no final caso o jogador perca.

# Bonequinho
# c) Utilize uma lista de strings para desenhar o boneco da forca. 
# Assim fica mais fácil caso o jogador erre para controlar cada parte.

bonequinho = ["""
__________
||       |
||       O
||      /|\\
||       |
||      / \\
||""","""
__________
||       |
||       O
||      /|\\
||       |
||      / 
||""","""
__________
||       |
||       O
||      /|\\
||       |
|| 
||""",
"""
__________
||       |
||       O
||      /|\\
||       
||       
||""",
"""
__________
||       |
||       O
||       |
||       
||      
||""",
"""
__________
||       |
||       O
||       
||       
||      
||""",
"""
__________
||       |
||       
||       
||       
||      
||"""]

# Erros
erros = 6

# A - Criar lista de palavras
palavrasDoJogo = ['Tinteiro', 'Cebolinha', 'Esquadro', 'Teriyaki', 'Valeriana', 'Violino']

# Contar numero de itens na lista com len
totalDePalavras = len(palavrasDoJogo) - 1

# B - Perguntar o número e escolher pelo indice
while True:
    escolha = int(input(f"Digite um número de 0 a {totalDePalavras}: "))

    if escolha <= totalDePalavras:
        break
    else:
        print(f'Número inválido, escolha um número entre 0 e {totalDePalavras}')

#escolha = 1

# Escolhe a palavra
palavraEscolhida = palavrasDoJogo[escolha].upper()

# contar caracteres da palavra
print( f"A palavra tem {len(palavraEscolhida)} letras.")
print(f'Você pode errar {erros} vezes')

# d) Apresentar a palavra no final caso o jogador perca.
letrasAcertadas = ''
letrasErradas = ''

while True:
    tentativa = input('Digite uma letra: ').upper()
    if( tentativa == '9' ):
        break

    # tentativa erradas são adicionadas a lista de Letras erradas e reduzem do tentativas possiveis
    if tentativa not in letrasErradas and tentativa not in palavraEscolhida:
        # Adiciona tentativa às letras erradas
        letrasErradas += tentativa

        print( f"Erros: {letrasErradas}({len( letrasErradas )})" )

        # Contabiliza o erro
        erros = erros - 1

    # tentativa que não tenham sido usadas nem estejam erradas - 
    elif tentativa not in letrasAcertadas:
        letrasAcertadas += tentativa

    # imprime o bonequinho na forca
    forca = f"{bonequinho[erros]}\n|| "
    venceu = True
    for letra in palavraEscolhida:
        if letra in letrasAcertadas:
            forca += f"{letra} "
        else:
            forca += '_ '
            venceu = False

    # Imprime a linha com as letras acertadas
    print( forca )

    # Se venceu, pode parar
    if venceu == True:
        print("=================\n||\n|| Você venceu! \n||")
        break

    # Parando o erro
    if erros == 0:
        print(f"Você perdeu. A palavra é {palavraEscolhida}.")
        break