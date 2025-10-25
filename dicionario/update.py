d1 = {'Pedro': 1000, 'Carlos': 750}
d2 = {'Ricardo': 2500, 'João': 1800}

for chave in d2:
    d1[chave] = d2[chave]

print(d1)