# QUESTÂO 2
estoque = 50  # Estoque inicial

while True:
    print("\n=== MENU DE CONTROLE DE ESTOQUE ===")
    print("1 - Vender Produto")
    print("2 - Comprar Produto")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        qtd = int(input("Digite a quantidade a vender: "))
        if qtd < 2:
            print("ERROR: A venda deve ser de pelo menos 2 produtos.")
        elif qtd > estoque:
            print(f"ERRO: Estoque insuficiente! Estoque atual: {estoque}")
        else:
            estoque -= qtd
            print(f"Venda realizada com sucesso! Estoque atual: {estoque}")

    elif opcao == "2":
        qtd = int(input("Digite a quantidade a comprar: "))
        if qtd < 2:
            print("ERROR: A compra deve ser de pelo menos 2 produtos.")
        elif estoque + qtd > 100:
            print(f"ERROR: Não é possível comprar. Limite máximo de 100 atingido! Estoque atual: {estoque}")
        else:
            estoque += qtd
            print(f"Compra realizada com sucesso! Estoque atual: {estoque}")

    elif opcao == "3":
        print("\nPrograma finalizado.")
        print(f"Estoque final: {estoque} produtos.")
        break

    else:
        print("Opção inválida. Tente novamente.")
