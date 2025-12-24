class Cliente:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def exibir_detalhes(self):
        print(f"Cliente: {self.nome} | Plano: {self.plano}")

lista_de_clientes = []

while True:
    nome = input("Digite o nome do cliente (ou 'sair'): ")
    if nome.lower() == 'sair':
        break

    plano = input("Digite o plano (Basic/Premium): ")

    novo_cliente = Cliente(nome, plano)
    lista_de_clientes.append(novo_cliente)

print("\n--- Relatório de Clientes Cadastrados ---")

for cliente in lista_de_clientes:
    cliente.exibir_detalhes()