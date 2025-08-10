maiorConsumo = 0
menorConsumo = 1000000

totalResidencial = 0
totalComercial = 0
totalIndustrial = 0

valorResidencial = 0
valorComercial = 0
valorIndustrial = 0

totalValor = 0
totalConsumo = 0

i = 0

while True:
    precoConsumido = float(input('Digite o Preço do KWh consumido: '))
    quantidadeConsumido = float(input('Digite a Quantidade Consumido durante o mês: '))
    tipoConsumidor = int(input('Digite o tipo do consumidor\n1- Residencial\n2- Comercial\n3 - industrial\nDigite aqui:'))

    if quantidadeConsumido > maiorConsumo:
        maiorConsumo = quantidadeConsumido

    if quantidadeConsumido < menorConsumo:
        menorConsumo = quantidadeConsumido

    valorGasto = precoConsumido * quantidadeConsumido

    if tipoConsumidor == 1:
        totalResidencial += quantidadeConsumido
        valorResidencial += valorGasto
    elif tipoConsumidor == 2:
        totalComercial += quantidadeConsumido
        valorComercial += valorGasto
    elif tipoConsumidor == 3:
        totalIndustrial += quantidadeConsumido
        valorIndustrial += valorGasto
    
    totalConsumo += quantidadeConsumido
    totalValor += valorGasto
    i+=1 #variavel de interação

    # condição de parada está aqui pq se eu digitar os valores, logo em seguida ele vai perguntar se desejo parar, caso deseje parar na primera interação ele não vai fazer toto processamento. O contrario acontece se eu colocar aqui em baixo
    op = input('Deseja continuar? (s/n):').lower() #.lower() isso garante com que tudo fique minusculo
    if op == 'n':
        break 

mediaConsumo = totalConsumo/i
mediaValor = totalValor/i

print(f'MAIOR consumo verificado: {maiorConsumo} KWh')
print(f'MENOR consumo verificado: {menorConsumo} KWh')

print(f'Total RESIDENCIAL: {totalResidencial} KWh | Valor gasto R$: {valorResidencial}')
print(f'Total COMERCIAL: {totalComercial} KWH | Valor gasto R$: {valorComercial}')
print(f'Total INDUSTRIAL: {totalIndustrial} KWh | Valor gasto R$ {valorIndustrial}')

print(f'MEDIA de consumo: {mediaConsumo:.2f}') #(:.2f) Dois pontos flutuantes apos a virgula (duas casas decimais)
print(f'MEDIA valor gasto: R${mediaValor:.2f}')
print(f'TOTAL valor gasto: R${totalValor:.2f}')

