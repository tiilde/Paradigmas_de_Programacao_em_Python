class personagem:
    def __init__(self, nome, elemento, level):
        self.nome = nome
        self.elemento = elemento
        self.level = level
        self.exp = 0
    
    def mudarElemento(self, novoElemento):
        self.elemento = novoElemento

    def mudarLevel (self, novoLevel):
        self.level = novoLevel

    def adicionarExp (self, novaExp):
        self.exp = self.exp + novaExp
    
    def conferirExp (self):
        if self.exp >= 100:
            self.level = self.level + 1
            self.exp = 0


venti = personagem('Venti Bla bla', "Anemo", 15 )

print("Nome:", venti.nome)
print("Elemento:", venti.elemento)

print()

personagemInicial = personagem("Blair", "Anemo", 39)
print("Nome:", personagemInicial.nome)
print("Elemento:", personagemInicial.elemento)
print("Level:", personagemInicial.level)
print("Exp:", personagemInicial.exp)
print()

personagemInicial.mudarElemento('Geo')
personagemInicial.adicionarExp(99)
personagemInicial.conferirExp()

print("Nome:", personagemInicial.nome)
print("Elemento:", personagemInicial.elemento)
print("Level:", personagemInicial.level)
print("Exp:", personagemInicial.exp)
print()

personagemInicial.adicionarExp(1)
personagemInicial.conferirExp()

print("Nome:", personagemInicial.nome)
print("Elemento:", personagemInicial.elemento)
print("Level:", personagemInicial.level)
print("Exp:", personagemInicial.exp)
