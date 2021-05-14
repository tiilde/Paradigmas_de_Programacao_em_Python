# Classe “BOMBA DE COMBUSTÍVEL”

# Faça um programa completo utilizando classes e métodos que:

# a) Possua uma classe chamada bombaCombustível, com no mínimo esses
# atributos:
# 1) tipoCombustivel.
# 2) valorLitro
# 3) quantidadeCombustivel
# b) Possua no mínimo esses métodos:
# 1) abastecerPorValor( ) – método onde é informado o valor a ser
# abastecido e mostra a quantidade de litros que foi colocada no
# veículo
# 2) abastecerPorLitro( ) – método onde é informado a quantidade
# em litros de combustível e mostra o valor a ser pago pelo cliente.
# 3) alterarValor( ) – altera o valor do litro do combustível.
# 4) alterarCombustivel( ) – altera o tipo do combustível.
# 5) alterarQuantidadeCombustivel( ) – altera a quantidade de
# combustível restante na bomba.


class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litrosNecessarios = valor / self.valorLitro
        if self.quantidadeCombustivel - litrosNecessarios >= 0:
            self.quantidadeCombustivel = self.quantidadeCombustivel - litrosNecessarios
            return litrosNecessarios
        else:
            print('Litros insuficientes na bomba!')
            return 0

    def abastecerPorLitro(self, quantidadeLitro):
        valorCobrado = quantidadeLitro * self.valorLitro
        if self.quantidadeCombustivel - quantidadeLitro >= 0:
            self.quantidadeCombustivel = self.quantidadeCombustivel - quantidadeLitro
            return valorCobrado
        else:
            print('Litros insuficientes na bomba!')
            return 0

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel
    
    def alterarQuantidadeCombustivel(self, novaQuantidadeCombustivel):
        self.quantidadeCombustivel = novaQuantidadeCombustivel



# Instanciando

bomba_01 = BombaCombustivel('Gasolina', 5, 200)
bomba_02 = BombaCombustivel('Diesel', 3, 200)
bomba_03 = BombaCombustivel('Etanol', 4, 200)



print("ABASTECENDO POR VALOR EM DINHEIRO\n")

abastecerValor = bomba_01.abastecerPorValor(20)
print("Litros abastecidos: ", abastecerValor, "L\n")
print("Combustível restante na bomba: ", bomba_01.quantidadeCombustivel, "L\n\n\n")

print("ABASTECENDO POR QUANTIDADE EM LITROS\n")

abastecerLitro = bomba_02.abastecerPorLitro(10)
print("Valor do abastecimento: R$", abastecerLitro, "\n")
print("Combustível restante na bomba: ", bomba_02.quantidadeCombustivel, "L\n\n\n")

print("ALTERANDO O VALOR DO LITRO DE COMBUSTÍVEL NA BOMBA\n")

print("Valor do litro na bomba:  R$", bomba_01.valorLitro, "\n")
bomba_01.alterarValor(8)
print("Novo valor do litro na bomba:  R$", bomba_01.valorLitro, "\n\n\n")

print("ALTERANDO O TIPO DE COMBUSTÍVEL\n")
bomba_01.alterarCombustivel('Etanol')
print("O combustível disponível é: ", bomba_01.tipoCombustivel, "\n\n\n")

print("ALTERANDO A QUANTIDADE DE COMBUSTÍVEL ARMAZENADO NA BOMBA\n")
bomba_01.alterarQuantidadeCombustivel(400)
print("Combustível disponível na bomba atualizado para:", bomba_01.quantidadeCombustivel, "L")

