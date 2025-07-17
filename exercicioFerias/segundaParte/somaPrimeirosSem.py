i = 1
soma = 0
expresao = ''
while i <= 100:
    soma += i

    expresao += str(i)
    if i < 100:
        expresao += '+'
    else:
        expresao += '='
    
    i+=1
    
print(f'{expresao}{soma}')