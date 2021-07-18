#Questão #2
#Escreva um programa que lê nome e idade de 5 pessoas e ao final informa quem é o mais novo, o mais velho e qual a média de idade. Faça o cálculo incluindo um método estático que leva em consideração um atributo estático com a lista de todas as pessoas.
class Pessoa:
    
    #criando um atributo estático
    populacao = 0
    lista_pessoas = []
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade   
        Pessoa.populacao += 1
        Pessoa.lista_pessoas = [] 
    
    @staticmethod
    def listapessoas(dados): #metodo estático
        Pessoa.lista_pessoas.append(dados)
        return Pessoa.lista_pessoas

dados = []

p1 = Pessoa('José',45)
dados.append(p1)
p2 = Pessoa('Maria',55)
dados.append(p2)
p3 = Pessoa('João',65)
dados.append(p3)


saida = []
saida = Pessoa.lista_pessoas(dados)
print(saida)