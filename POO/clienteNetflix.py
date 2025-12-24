listaPlanos = ['basic', 'premium']

class Clientes:
    def __init__(self, nome, idade, email, plano):
        self.nome = nome
        self.idade = idade
        self.email = email

        self.listaPlanos = ['basic', 'premium']
        if plano not in listaPlanos:
            print('plano INVALIDO')
        else:
            self.plano = plano

    def mudar_plano(self, novoPlano):
        if novoPlano in listaPlanos:
            self.plano = novoPlano
        else:
            print('Erro: plano invalido')

    def __str__(self):
        return f'{self.nome}: {self.idade}, {self.email}, {self.plano}'

cli1 = Clientes('Emerson', '18', 'emerson@gmail.com', 'premium')
print(cli1.plano)
cli1.mudar_plano('basic')
print(cli1.plano)