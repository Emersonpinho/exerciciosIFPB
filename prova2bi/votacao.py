# QUESTÃO 4
joao = 0
maria = 0
nulo = 0
branco = 0
total = 0

while True:
    print("\n=== MENU DE VOTAÇÃO ===")
    print("1 - Candidato João")
    print("2 - Candidato Maria")
    print("3 - Voto Nulo")
    print("4 - Voto em Branco")
    print("0 - Encerrar Votação")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        joao += 1
        total += 1
        print("Voto registrado para João.")
    elif opcao == "2":
        maria += 1
        total += 1
        print("Voto registrado para Maria.")
    elif opcao == "3":
        nulo += 1
        total += 1
        print("Voto Nulo registrado.")
    elif opcao == "4":
        branco += 1
        total += 1
        print("Voto em Branco registrado.")
    elif opcao == "0":
        print("\nVotação encerrada!")
        break
    else:
        print("Opção inválida. Tente novamente.")

if total > 0:
    perc_nulo = (nulo / total) * 100
    perc_branco = (branco / total) * 100
else:
    perc_nulo = perc_branco = 0

print("\n=== RESULTADO FINAL ===")
print(f"Total de votos: {total}")
print(f"João: {joao} votos")
print(f"Maria: {maria} votos")
print(f"Nulos: {nulo} votos ({perc_nulo:.2f}%)")
print(f"Brancos: {branco} votos ({perc_branco:.2f}%)")
