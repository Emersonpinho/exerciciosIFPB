class Controle:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentando o canal")
        else:
            print("Diminuindo o canal")

    def __str__(self):
        return f"Controle: {self.cor}, {self.altura}, {self.largura}, {self.profundidade}"

controle1 = Controle("Cinza", "10cm", "2cm", "2cm")
controle1.passar_canal("+")

