def saudacao(resposta):
    match resposta:
        case 1:
            return "oi"
        case 2:
            return "olá"
        case 3:
            return "Bom dia"
        case _:
            return 'ok'
     
a = int(input('Digite um número: '))

print(saudacao(a))
        

