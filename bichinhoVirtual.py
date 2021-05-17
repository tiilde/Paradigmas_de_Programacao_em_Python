# Classe “BICHINHO VIRTUAL”

# Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# a) Atributos: Nome, Fome, Saúde e Idade

# b) Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome,
# Saúde e Idade

# Obs: Existe mais uma informação que devemos levar em consideração, o
# Humor do nosso tamagushi, este humor é uma combinação entre os
# atributos Fome e Saúde, ou seja, um campo calculado, então não devemos
# criar um atributo para armazenar esta informação por que ela pode ser
# calculada a qualquer momento.

# c) Melhore o programa do bichinho virtual, permitindo que o usuário
# especifique quanto de comida ele fornece ao bichinho e por quanto
# tempo ele brinca com o bichinho. Faça com que estes valores afetem
# quão rapidamente os níveis de fome e tédio caem.

# d) Crie uma "porta escondida" no programa do programa do bichinho
# virtual que mostre os valores exatos dos atributos do objeto. Consiga
# isto mostrando o objeto quando uma opção secreta, não listada no
# menu, for informada na escolha do usuário. Dica: acrescente um
# método especial str() à classe Bichinho.


class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def setNome(self, novoNome):
        self.nome = novoNome
        return self.nome

    def setFome(self, valorFome):
        self.fome = valorFome
        return self.fome

    def setSaude(self, valorSaude):
        self.saude = valorSaude
        return self.saude

    def setIdade(self, valorIdade):
        self.idade = valorIdade
        return self.idade

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude

    def getIdade(self):
        return self.idade

    # Humor do bichinho baseado nos atributos fome e saúde.

    def humor(self):
        statusHumor = (self.fome + self.saude) / 2

        if statusHumor >= -10:
            humor = 'Com raiva'
        if statusHumor >= -5:
            humor = 'Mau humor'
        if statusHumor >= 0:
            humor = 'Ok'
        if statusHumor >= 5:
            humor = 'Animado'
        if statusHumor == 10:
            humor = 'Feliz'
        return statusHumor

    # É pego o valor da fome atual e é adicionado o valor da comida
    # o valor máximo da fome será 10.

    def alimentar(self, comida):
        if self.fome < 10:
            self.fome = self.fome + comida
            if self.fome > 10:
                self.fome = 10
            return self.fome
        else:
            return f'{self.nome} está de barriga cheia.'

    def brincar(self, tempoBrincando):
        if self.saude < 10:
            self.saude = self.saude + tempoBrincando
            if self.saude > 10:
                self.saude = 10
            return self.saude
        else:
            return f'{self.nome} não quer brincar agora, tente brincar depois.'


         
    # Método que mostra todas as informações do bichinho, usando método str.

    def __str__(self):
        return f'Valores exatos dos atributos do objeto: \n\nNome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}\n\n'




# Instanciando o objeto

# bibi = BichinhoVirtual('', 0, 0, 0)
# # exibindo o objeto com os atributos iniciais
# print(bibi)

# bibi = BichinhoVirtual('Bibi', 0, 0, 4)
# # humor
# print('Exibindo o humor do bichinho virtual')
# print(bibi.humor(), "\n\n")

# print("Alimentando o bichinho virtual")
# print(bibi.alimentar(3))
# print(bibi.alimentar(4), "\n\n")

# print("Brincando com o bichinho virtual")
# print(bibi.brincar(3))
# print(bibi.brincar(3), "\n\n")

# print("Exibindo o humor do bichinho virtual")
# # humor
# print(bibi.humor(), "\n\n")

# # exibindo atributos do bichinho após sofrer alterações
# print(bibi)

# print("ALTERANDO A FOME DO BICHINHO")
# print(bibi.setFome(8))
# print("ALTERANDO A SAÚDE DO BICHINHO")
# print(bibi.setSaude(7))
# print("ALTERANDO A IDADE DO BICHINHO")
# print(bibi.setIdade(6))
# print("EXIBINDO O HUMOR DO BICHINHO APÓS AS ALTERAÇÕES")
# print(bibi.humor())
# print("ALTERANDO O NOME DO BICHINHO")
# print(bibi.setNome('Bibizinha'), "\n")


# print(bibi)

