__author__ = 'Flavios'

class Pessoa:

    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def __str__(self):
        return self.nome + ' '+self.sobrenome+' '+str(self.idade)

    def iniciais(self):
        return self.nome[0]+self.sobrenome[0]

    def mudaIdade(self,valor):
        self.idade +=valor

esposa = Pessoa('Ana Paula','Gonçalves',20)
print(esposa)
esposa.mudaIdade(2)
print(esposa)
print(esposa.iniciais())