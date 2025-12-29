class Canal:
    #metedo construtor / metodo magico
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos

    def mostrar(self):
        return f'Canal: {self.nome}\nDescrição: {self.descricao}\nInscritos: {self.inscritos}'

canal1 = Canal('lanCode', 'Canal legalzinho para estudar programação', '2M')

print(canal1.mostrar())