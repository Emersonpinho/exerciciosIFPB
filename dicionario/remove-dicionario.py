d = {'Pedro': 1000, 'Carlos': 750, 'Ricardo': 2500}

nova = {} 
op = input('Digite o a chave que deseja apagar: ') # novo dicionário vazio
for chave in d:
    if chave != op:  # mantemos todas as chaves **menos** a que queremos remover
        nova[chave] = d[chave]

print(nova)