class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e dépositos
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"ID: {self.id}, Titular: {self.titular}, Saldo: R${self.saldo:.2f}"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:.2f} Autorizado para conta f{self.id}!!")

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} Autorizado para conta {self.id}!!")
        else:
            print(f"A conta {self.id} está com saldo insuficiente para transação!!!!")


conta1 = ContaBancaria(112, "hermano", 4506)
conta1.sacar(600)
print(conta1)