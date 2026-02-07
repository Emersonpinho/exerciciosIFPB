# Declaração das classes
class Gafanhoto:
    """
Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

para criar uma nova pessoa, use
variavel =  gafanhoto(nome, idade)

    """
    def __init__(self, nome = "Vazio", idade = 0): # Metodo construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): # Dunder method
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: Nome = {self.nome}; Idade = {self.idade}"

# Declaração de objetos
g1 = Gafanhoto("Claudivan", 65)
g1.aniversario()
# print(g1)

print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method
print(g1.__class__)
print(g1.__doc__) # Dunder attribute

