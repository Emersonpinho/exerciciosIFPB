num1 = int(input("Digite um Número: "))
num2 = int(input("Digite o segundo Número: "))

operacao = str(input("Qual operação deseja fazer? (+, -, *, /): "))

if operacao == "+":
    print(f"A soma de {num1} + {num2} é igual à: {num1+num2}")
elif operacao == "-":
    print(f"A Subtração de {num1} - {num2} é igual à: {num1-num2}")
elif operacao == "*":
    print(f"A multiplicação de {num1} * {num2} é igual à: {num1*num2}")
elif operacao == "/":
    if num2 == 0:
        print("Erro: Divisão por zero!")
    else:
        print(f"A divisão de {num1} / {num2} é igual à: {num1/num2:.2f}")